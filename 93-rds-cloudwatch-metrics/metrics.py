import os,boto3
from datetime import datetime,timezone,timedelta
cw=boto3.client("cloudwatch"); now=datetime.now(timezone.utc)
r=cw.get_metric_statistics(Namespace="AWS/RDS",MetricName="CPUUtilization",Dimensions=[{"Name":"DBInstanceIdentifier","Value":os.environ["DB_INSTANCE"]}],StartTime=now-timedelta(hours=1),EndTime=now,Period=300,Statistics=["Average"])
for x in r["Datapoints"]: print(x)