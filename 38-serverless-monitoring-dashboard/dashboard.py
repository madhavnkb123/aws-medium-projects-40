import os,json,boto3
from datetime import datetime,timezone,timedelta
now=datetime.now(timezone.utc)
r=boto3.client("cloudwatch").get_metric_statistics(Namespace=os.environ.get("NAMESPACE","AWS/Lambda"),MetricName=os.environ.get("METRIC_NAME","Invocations"),Dimensions=[{"Name":"FunctionName","Value":os.environ["FUNCTION_NAME"]}],StartTime=now-timedelta(hours=1),EndTime=now,Period=300,Statistics=["Sum"])
print(json.dumps(sorted(r["Datapoints"],key=lambda x:x["Timestamp"]),default=str,indent=2))