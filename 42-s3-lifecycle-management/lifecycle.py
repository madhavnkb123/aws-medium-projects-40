import os,boto3
s3=boto3.client("s3"); bucket=os.environ["BUCKET"]
rules=[{"ID":"archive-old-objects","Status":"Enabled","Filter":{"Prefix":os.environ.get("PREFIX","")}, "Transitions":[{"Days":30,"StorageClass":"STANDARD_IA"},{"Days":90,"StorageClass":"GLACIER"}]}]
s3.put_bucket_lifecycle_configuration(Bucket=bucket,LifecycleConfiguration={"Rules":rules})
print("Lifecycle policy configured")