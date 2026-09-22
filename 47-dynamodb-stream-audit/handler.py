def lambda_handler(event,context):
 for r in event.get("Records",[]):
  print(r.get("eventName"),r.get("dynamodb",{}))
 return {"processed":len(event.get("Records",[]))}