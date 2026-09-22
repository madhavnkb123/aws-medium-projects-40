import os,io,boto3,pandas as pd
s3=boto3.client("s3"); b=os.environ["S3_BUCKET"]
df=pd.read_csv(io.BytesIO(s3.get_object(Bucket=b,Key=os.environ["INPUT_KEY"])["Body"].read()))
out=df.describe(include="all").transpose().reset_index()
buf=io.StringIO(); out.to_csv(buf,index=False)
key=os.environ.get("OUTPUT_KEY","output/summary.csv")
s3.put_object(Bucket=b,Key=key,Body=buf.getvalue().encode()); print("Wrote",key)