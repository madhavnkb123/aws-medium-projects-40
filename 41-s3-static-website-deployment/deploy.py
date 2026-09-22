import os,boto3
s3=boto3.client("s3"); bucket=os.environ["BUCKET"]; root=os.environ["SITE_DIR"]
for name in os.listdir(root):
 p=os.path.join(root,name)
 if os.path.isfile(p): s3.upload_file(p,bucket,name,ExtraArgs={"ContentType":"text/html" if name.endswith(".html") else "application/octet-stream"})
print("Website files uploaded")