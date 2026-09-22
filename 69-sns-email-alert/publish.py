import os,boto3
r=boto3.client("sns").publish(TopicArn=os.environ["TOPIC_ARN"],Subject=os.environ.get("SUBJECT","Production Alert"),Message=os.environ["MESSAGE"])
print(r["MessageId"])