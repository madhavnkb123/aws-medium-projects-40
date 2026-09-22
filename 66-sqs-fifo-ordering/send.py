import os,boto3
r=boto3.client("sqs").send_message(QueueUrl=os.environ["QUEUE_URL"],MessageBody=os.environ["MESSAGE"],MessageGroupId=os.environ.get("MESSAGE_GROUP","orders"),MessageDeduplicationId=os.environ.get("DEDUP_ID","demo-1"))
print(r["MessageId"])