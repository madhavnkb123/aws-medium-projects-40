import os,boto3
from boto3.dynamodb.conditions import Key
t=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
r=t.query(IndexName=os.environ["INDEX_NAME"],KeyConditionExpression=Key(os.environ["INDEX_KEY"]).eq(os.environ["INDEX_VALUE"]))
for x in r["Items"]: print(x)