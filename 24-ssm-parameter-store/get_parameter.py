import os,boto3
r=boto3.client("ssm").get_parameter(Name=os.environ["PARAMETER_NAME"],WithDecryption=True)
v=r["Parameter"]["Value"]; print("Parameter loaded; length:",len(v))
if os.environ.get("PRINT_VALUE")=="true": print(v)