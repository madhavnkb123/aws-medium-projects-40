import os,boto3
value=float(os.environ.get("METRIC_VALUE","75"))
boto3.client("cloudwatch").put_metric_data(Namespace=os.environ.get("NAMESPACE","Training/App"),MetricData=[{"MetricName":"DemoMetric","Value":value,"Unit":"Count"}])
print("Published:",value)