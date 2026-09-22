import boto3
r=boto3.client("ssm").describe_instance_information()
for x in r["InstanceInformationList"]: print(x["InstanceId"],x["PingStatus"],x.get("PlatformName"),x.get("AgentVersion"))