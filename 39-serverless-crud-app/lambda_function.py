import os,json,uuid,boto3
t=boto3.resource("dynamodb").Table(os.environ["TABLE_NAME"])
def out(c,b): return {"statusCode":c,"headers":{"Content-Type":"application/json"},"body":json.dumps(b)}
def lambda_handler(e,c):
    m=e.get("requestContext",{}).get("http",{}).get("method",e.get("httpMethod","GET")); p=e.get("pathParameters") or {}
    if m=="POST":
        d=json.loads(e.get("body") or "{}"); item={"id":str(uuid.uuid4()),"name":d.get("name","item")}; t.put_item(Item=item); return out(201,item)
    if m=="GET" and p.get("id"): return out(200,t.get_item(Key={"id":p["id"]}).get("Item",{}))
    if m=="GET": return out(200,t.scan().get("Items",[]))
    if m=="DELETE" and p.get("id"): t.delete_item(Key={"id":p["id"]}); return out(204,{})
    return out(405,{"error":"method not supported"})