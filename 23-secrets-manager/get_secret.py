import os,boto3
r=boto3.client("secretsmanager").get_secret_value(SecretId=os.environ["SECRET_ID"])
value=r.get("SecretString",r.get("SecretBinary",""))
print("Secret retrieved; length:",len(value))
if os.environ.get("PRINT_SECRET")=="true": print(value)