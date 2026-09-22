import json
def lambda_handler(event,context):
    body=event.get("body")
    if isinstance(body,str):
        try: body=json.loads(body)
        except json.JSONDecodeError: pass
    m=event.get("requestContext",{}).get("http",{}).get("method",event.get("httpMethod","GET"))
    return {"statusCode":200,"headers":{"Content-Type":"application/json"},"body":json.dumps({"method":m,"message":"Hello from Lambda","body":body})}