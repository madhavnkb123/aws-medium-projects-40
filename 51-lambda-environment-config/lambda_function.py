import os
def lambda_handler(event,context):
 return {"statusCode":200,"body":f"Environment: {os.environ.get('APP_ENV','dev')}"} 