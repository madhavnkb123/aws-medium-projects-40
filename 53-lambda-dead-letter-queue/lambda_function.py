import os
def lambda_handler(event,context):
 if os.environ.get("FAIL","false")=="true": raise RuntimeError("Intentional failure for DLQ testing")
 return {"ok":True}