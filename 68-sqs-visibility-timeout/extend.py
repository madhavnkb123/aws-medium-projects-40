import os,boto3
sqs=boto3.client("sqs")
sqs.change_message_visibility(QueueUrl=os.environ["QUEUE_URL"],ReceiptHandle=os.environ["RECEIPT_HANDLE"],VisibilityTimeout=int(os.environ.get("TIMEOUT","120")))
print("Visibility timeout extended")