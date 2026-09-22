import os,json,uuid,boto3
t=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
def lambda_handler(e,c):
    m=e.get("requestContext",{}).get("http",{}).get("method",e.get("httpMethod","GET")); p=e.get("pathParameters") or {}
    if m=="POST":
        d=json.loads(e.get("body") or "{}"); item={"id":str(uuid.uuid4()),"name":d.get("name","demo")}; t.put_item(Item=item); return {"statusCode":201,"body":json.dumps(item)}
    if m=="GET": return {"statusCode":200,"body":json.dumps(t.get_item(Key={"id":p.get("id","")}).get("Item",{}))}
    if m=="DELETE": t.delete_item(Key={"id":p["id"]}); return {"statusCode":204,"body":""}
    return {"statusCode":405,"body":"Method not supported"}