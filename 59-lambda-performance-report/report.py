import os,boto3
cw=boto3.client("cloudwatch")
for metric in ["Invocations","Errors","Duration"]:
 r=cw.get_metric_statistics(Namespace="AWS/Lambda",MetricName=metric,Dimensions=[{"Name":"FunctionName","Value":os.environ["FUNCTION_NAME"]}],StartTime=__import__("datetime").datetime.now(__import__("datetime").timezone.utc)-__import__("datetime").timedelta(hours=1),EndTime=__import__("datetime").datetime.now(__import__("datetime").timezone.utc),Period=300,Statistics=["Average","Sum"])
 print(metric,len(r["Datapoints"]))