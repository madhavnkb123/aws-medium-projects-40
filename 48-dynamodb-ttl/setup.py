import os,boto3
boto3.client("dynamodb").update_time_to_live(TableName=os.environ["TABLE_NAME"],TimeToLiveSpecification={"Enabled":True,"AttributeName":os.environ.get("TTL_ATTRIBUTE","expiresAt")})
print("TTL enabled")