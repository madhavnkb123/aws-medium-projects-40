import boto3
s3=boto3.client("s3")
for b in s3.list_buckets()["Buckets"]:
 try: enc=s3.get_bucket_encryption(Bucket=b["Name"])["ServerSideEncryptionConfiguration"]["Rules"]; print(b["Name"],"ENCRYPTED")
 except s3.exceptions.ClientError: print(b["Name"],"CHECK ENCRYPTION")