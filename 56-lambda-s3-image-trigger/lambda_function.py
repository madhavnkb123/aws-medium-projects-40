import urllib.parse
def lambda_handler(event,context):
 for r in event.get("Records",[]):
  key=urllib.parse.unquote_plus(r["s3"]["object"]["key"])
  if key.lower().endswith((".jpg",".jpeg",".png",".webp")): print("Image received:",key)
 return {"ok":True}