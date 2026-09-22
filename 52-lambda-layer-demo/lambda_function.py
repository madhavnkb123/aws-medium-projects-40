def lambda_handler(event,context):
 try:
  import requests
  return {"statusCode":200,"body":f"requests={requests.__version__}"}
 except ImportError: return {"statusCode":500,"body":"Attach a Lambda layer containing requests"}