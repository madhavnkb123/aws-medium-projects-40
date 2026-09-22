import os,boto3
r=boto3.client("logs").start_query(logGroupName=os.environ["LOG_GROUP"],startTime=int(__import__("time").time())-3600,endTime=int(__import__("time").time()),queryString=os.environ.get("QUERY","fields @timestamp,@message | limit 20"))
print("QueryId:",r["queryId"])