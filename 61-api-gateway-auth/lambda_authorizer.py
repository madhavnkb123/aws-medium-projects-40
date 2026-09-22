import os
def lambda_handler(event,context):
 token=event.get("headers",{}).get("authorization","")
 allow=token==os.environ.get("API_TOKEN","demo-token")
 return {"isAuthorized":allow,"context":{"source":"custom-authorizer"}}