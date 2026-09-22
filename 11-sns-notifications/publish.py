import os,boto3
r=boto3.client("sns").publish(TopicArn=os.environ["TOPIC_ARN"],Subject=os.environ.get("SUBJECT","AWS Notification"),Message=os.environ.get("MESSAGE","Hello from SNS"))
print(r["MessageId"])