import os,boto3
boto3.client("cloudwatch").put_metric_alarm(AlarmName=os.environ.get("ALARM_NAME","DemoAlarm"),Namespace=os.environ.get("NAMESPACE","Training/App"),MetricName="DemoMetric",Statistic="Average",Period=300,EvaluationPeriods=1,Threshold=float(os.environ.get("THRESHOLD","100")),ComparisonOperator="GreaterThanThreshold",ActionsEnabled=False)
print("Alarm created")