def lambda_handler(event,context):
 for r in event.get("Records",[]): print("DLQ message:",r.get("body"))
 return {"count":len(event.get("Records",[]))}