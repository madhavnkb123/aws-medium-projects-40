def lambda_handler(event,context):
 detail=event.get("detail",{})
 print("Event type:",event.get("detail-type"),"detail:",detail)
 return {"routed":True}