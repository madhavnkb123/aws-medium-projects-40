import os,boto3
t=boto3.resource("dynamodb").Table(os.environ["IDEMPOTENCY_TABLE"])
def lambda_handler(event,context):
 key=str(event["idempotency_key"])
 if t.get_item(Key={"id":key}).get("Item"): return {"status":"duplicate"}
 t.put_item(Item={"id":key,"status":"processed"})
 return {"status":"processed"}