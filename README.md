# ElasticSeach Utils

This is (going to be) a small collection of tools I've build to work with [ElasticSearch](https://www.elastic.co/).

## ElasticUsage

This tool shows an overall cluster usage of storage. This was pretty usefull for me to plan future cluster growth and make sizings for new clusters.

```bash
./elasticusage.py -n elasticnode01
Total: 16.8TiB
Free:  12.9TiB
Used:  3.9TiB
```

Please not again that it shows **NOT** only the storage on the node you specify. This is the total/free/used storage by your whole cluster
