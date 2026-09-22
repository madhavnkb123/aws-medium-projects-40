import os,boto3,time
ddb=boto3.client("dynamodb"); name=os.environ["TABLE_NAME"]
r=ddb.create_backup(TableName=name,BackupName=f"{name}-{int(time.time())}")
print(r["BackupDetails"]["BackupArn"])