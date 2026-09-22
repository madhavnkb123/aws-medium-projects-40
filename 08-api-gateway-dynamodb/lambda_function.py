import os,json,uuid,boto3
t=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
def lambda_handler(e,c):
    d=json.loads(e.get("body") or "{}"); item={"id":d.get("id",str(uuid.uuid4())),"name":d.get("name","unnamed")}
    t.put_item(Item=item)
    return {"statusCode":201,"headers":{"Content-Type":"application/json"},"body":json.dumps(item)}