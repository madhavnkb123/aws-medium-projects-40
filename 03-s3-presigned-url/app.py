import os,boto3
s3=boto3.client("s3")
url=s3.generate_presigned_url("get_object",Params={"Bucket":os.environ["S3_BUCKET"],"Key":os.environ["S3_KEY"]},ExpiresIn=int(os.environ.get("URL_TTL","900")))
print(url)