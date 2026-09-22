import os,boto3
r=boto3.client("sqs").send_message(QueueUrl=os.environ["QUEUE_URL"],MessageBody=os.environ.get("MESSAGE","hello from boto3"))
print("MessageId:",r["MessageId"])