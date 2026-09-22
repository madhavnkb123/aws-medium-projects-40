import json,datetime
def lambda_handler(event,context):
 print(json.dumps({"level":"INFO","time":datetime.datetime.now(datetime.timezone.utc).isoformat(),"message":"request_processed"}))
 return {"ok":True}