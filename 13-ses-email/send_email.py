import os,boto3
ses=boto3.client("ses",region_name=os.environ.get("AWS_REGION","us-east-1"))
r=ses.send_email(Source=os.environ["FROM_EMAIL"],Destination={"ToAddresses":[os.environ["TO_EMAIL"]]},Message={"Subject":{"Data":os.environ.get("SUBJECT","AWS SES Test")},"Body":{"Text":{"Data":os.environ.get("BODY","Hello from Amazon SES.")}}})
print(r["MessageId"])