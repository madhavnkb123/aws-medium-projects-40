import os,boto3
s3=boto3.client("s3"); source=os.environ["SOURCE_BUCKET"]; target=os.environ["LOG_BUCKET"]
s3.put_bucket_logging(Bucket=source,BucketLoggingStatus={"LoggingEnabled":{"TargetBucket":target,"TargetPrefix":"access-logs/"}})
print("S3 access logging enabled")