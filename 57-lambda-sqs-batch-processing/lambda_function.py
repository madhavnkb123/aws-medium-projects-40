def lambda_handler(event,context):
 failures=[]
 for r in event.get("Records",[]):
  try: print("Processing",r["messageId"],r["body"])
  except Exception: failures.append({"itemIdentifier":r["messageId"]})
 return {"batchItemFailures":failures}