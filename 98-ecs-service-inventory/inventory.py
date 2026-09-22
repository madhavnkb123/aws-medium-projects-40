import os,boto3
ecs=boto3.client("ecs")
for c in ecs.list_clusters()["clusterArns"]:
 for s in ecs.list_services(cluster=c)["serviceArns"]:
  x=ecs.describe_services(cluster=c,services=[s])["services"][0]
  print(x["serviceName"],x["desiredCount"],x["runningCount"],x["status"])