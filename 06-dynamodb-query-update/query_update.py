import os,boto3
from boto3.dynamodb.conditions import Key
t=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"]); pk=os.environ["PARTITION_KEY_VALUE"]
name=os.environ.get("PARTITION_KEY","pk")
r=t.query(KeyConditionExpression=Key(name).eq(pk)); print(r["Items"])
if r["Items"]:
    t.update_item(Key={name:pk},UpdateExpression="SET #s=:v",ExpressionAttributeNames={"#s":"status"},ExpressionAttributeValues={":v":"updated"})
    print("Updated",pk)