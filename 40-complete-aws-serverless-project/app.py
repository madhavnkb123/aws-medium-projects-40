import os,json,uuid,boto3
ddb=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"]); sns=boto3.client("sns")
def handler(event,context):
    method=event.get("requestContext",{}).get("http",{}).get("method","GET")
    if method=="POST":
        data=json.loads(event.get("body") or "{}"); item={"id":str(uuid.uuid4()),"title":data.get("title","Task"),"status":"OPEN"}
        ddb.put_item(Item=item)
        if os.environ.get("TOPIC_ARN"): sns.publish(TopicArn=os.environ["TOPIC_ARN"],Message=json.dumps(item))
        return {"statusCode":201,"body":json.dumps(item)}
    return {"statusCode":200,"body":json.dumps(ddb.scan().get("Items",[]))}