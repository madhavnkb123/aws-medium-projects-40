import boto3
ec2=boto3.client("ec2")
for r in ec2.describe_instances(Filters=[{"Name":"instance-state-name","Values":["stopped"]}])["Reservations"]:
    for i in r["Instances"]: print("Review stopped instance:",i["InstanceId"],i["InstanceType"])
print("Extend this scanner with EBS, Elastic IP and idle-resource checks before automating cleanup.")