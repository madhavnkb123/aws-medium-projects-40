import boto3
for r in boto3.client("ec2").describe_instances()["Reservations"]:
    for i in r["Instances"]: print(i["InstanceId"],i["State"]["Name"],i["InstanceType"],i.get("PrivateIpAddress","-"))