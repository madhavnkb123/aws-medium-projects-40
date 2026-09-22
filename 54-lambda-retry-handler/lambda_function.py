import random
def lambda_handler(event,context):
 if random.random()<float(event.get("failure_rate",0)): raise RuntimeError("Retryable demo failure")
 return {"processed":True}