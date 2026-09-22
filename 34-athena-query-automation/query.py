import os,time,boto3
ath=boto3.client("athena")
qid=ath.start_query_execution(QueryString=os.environ["QUERY"],QueryExecutionContext={"Database":os.environ["DATABASE"]},ResultConfiguration={"OutputLocation":os.environ["OUTPUT_S3"]})["QueryExecutionId"]
while True:
    s=ath.get_query_execution(QueryExecutionId=qid)["QueryExecution"]["Status"]["State"]
    if s in ("SUCCEEDED","FAILED","CANCELLED"): break
    time.sleep(2)
print("Query",qid,s)
if s=="SUCCEEDED":
    for row in ath.get_query_results(QueryExecutionId=qid)["ResultSet"]["Rows"]: print([d.get("VarCharValue","") for d in row["Data"]])