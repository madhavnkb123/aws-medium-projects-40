import boto3
for d in boto3.client("rds").describe_db_instances()["DBInstances"]:
 print(d["DBInstanceIdentifier"],d["Engine"],d["DBInstanceStatus"],d["DBInstanceClass"])