def lambda_handler(event,context):
    for record in event.get("Records",[]): print("Processing:",record.get("body"))
    return {"processed":len(event.get("Records",[]))}