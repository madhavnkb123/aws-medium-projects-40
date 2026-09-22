import os,boto3
ecs=boto3.client("ecs")
r=ecs.describe_task_definition(taskDefinition=os.environ["TASK_DEFINITION"])["taskDefinition"]
print(r["family"],r["revision"],r["cpu"],r["memory"])
for c in r["containerDefinitions"]: print(c["name"],c.get("image"))