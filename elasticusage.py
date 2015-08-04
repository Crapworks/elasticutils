#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import urllib2
import json


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


class ElasticUsage(object):
    def __init__(self, node, port=9200, proto='http'):
        self.url = '%s://%s:%s/_nodes/stats' % (proto, node, port)
        self.total = 0
        self.free = 0
        self._usage()

    def _usage(self):
        resp = urllib2.urlopen(self.url)
        stats = json.load(resp)
        for nodes, content in stats['nodes'].iteritems():
            if content['fs']['total']:
                self.total += int(content['fs']['total']['total_in_bytes'])
                self.free += int(content['fs']['total']['free_in_bytes'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--node', help='hostname of an es node', required=True)
    parser.add_argument('-p', '--port', help='port to connect to (def: 9200)', default=9200)
    parser.add_argument('-t', '--proto', help='protocol to use (def: http)', default='http')
    args = parser.parse_args()

    try:
        usage = ElasticUsage(node=args.node, port=args.port, proto=args.proto)
    except urllib2.URLError as err:
        print "urlerror: %s" % (err.reason, )
    else:
        print "Total: %s" % (sizeof_fmt(usage.total), )
        print "Free:  %s" % (sizeof_fmt(usage.free) ,)
        print "Used:  %s" % (sizeof_fmt(usage.total - usage.free) ,)


if __name__ == '__main__':
    main()
