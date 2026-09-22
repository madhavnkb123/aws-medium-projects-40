import os,boto3
ecs=boto3.client("ecs")
x=ecs.describe_services(cluster=os.environ["CLUSTER"],services=[os.environ["SERVICE"]])["services"][0]
print("Service:",x["serviceName"],"desired:",x["desiredCount"],"running:",x["runningCount"],"pending:",x["pendingCount"],"task_definition:",x["taskDefinition"])