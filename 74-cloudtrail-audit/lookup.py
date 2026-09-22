import os,boto3
ct=boto3.client("cloudtrail")
r=ct.lookup_events(LookupAttributes=[{"AttributeKey":"Username","AttributeValue":os.environ["USERNAME"]}],MaxResults=10)
for e in r["Events"]: print(e["EventTime"],e["EventName"],e["Username"])