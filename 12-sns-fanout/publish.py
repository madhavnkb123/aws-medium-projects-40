import os,json,boto3
payload={"event":"order_created","order_id":os.environ.get("ORDER_ID","1001")}
r=boto3.client("sns").publish(TopicArn=os.environ["TOPIC_ARN"],Message=json.dumps(payload))
print("Fan-out message:",r["MessageId"])