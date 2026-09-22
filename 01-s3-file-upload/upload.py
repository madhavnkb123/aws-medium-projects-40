import os,boto3
s3=boto3.client("s3")
path=os.environ.get("LOCAL_FILE","sample.txt")
bucket=os.environ["S3_BUCKET"]; key=os.environ.get("S3_KEY",os.path.basename(path))
s3.upload_file(path,bucket,key)
print(f"Uploaded s3://{bucket}/{key}")