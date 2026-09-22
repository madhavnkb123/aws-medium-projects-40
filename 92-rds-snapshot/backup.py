import os,boto3,time
r=boto3.client("rds").create_db_snapshot(DBSnapshotIdentifier=f"{os.environ['DB_INSTANCE']}-{int(time.time())}",DBInstanceIdentifier=os.environ["DB_INSTANCE"])
print(r["DBSnapshot"]["DBSnapshotIdentifier"])