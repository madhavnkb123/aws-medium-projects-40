import os,boto3
boto3.client("logs").put_retention_policy(logGroupName=os.environ["LOG_GROUP"],retentionInDays=int(os.environ.get("RETENTION_DAYS","30")))
print("Retention configured")