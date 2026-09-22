import os,boto3
g=boto3.client("glue")
for db in g.get_databases()["DatabaseList"]: print("DATABASE",db["Name"])
if os.environ.get("DATABASE"):
    for t in g.get_tables(DatabaseName=os.environ["DATABASE"])["TableList"]: print("TABLE",t["Name"],t["StorageDescriptor"].get("Location"))