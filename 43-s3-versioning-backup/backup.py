import os,boto3
s3=boto3.client("s3"); b=os.environ["BUCKET"]
s3.put_bucket_versioning(Bucket=b,VersioningConfiguration={"Status":"Enabled"})
print("Versioning enabled:",b)