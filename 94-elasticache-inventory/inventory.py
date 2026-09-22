import boto3
for x in boto3.client("elasticache").describe_cache_clusters()["CacheClusters"]:
 print(x["CacheClusterId"],x["Engine"],x["CacheClusterStatus"],x["CacheNodeType"])