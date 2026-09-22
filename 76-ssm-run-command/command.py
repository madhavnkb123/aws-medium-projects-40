import os,boto3
r=boto3.client("ssm").send_command(InstanceIds=[os.environ["INSTANCE_ID"]],DocumentName=os.environ.get("DOCUMENT","AWS-RunShellScript"),Parameters={"commands":[os.environ.get("COMMAND","echo hello")]})
print("CommandId:",r["Command"]["CommandId"])