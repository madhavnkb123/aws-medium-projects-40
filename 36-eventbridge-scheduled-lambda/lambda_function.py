import datetime
def lambda_handler(event,context):
    print("Scheduled invocation:",datetime.datetime.now(datetime.timezone.utc).isoformat())
    print("Event:",event)
    return {"ok":True}