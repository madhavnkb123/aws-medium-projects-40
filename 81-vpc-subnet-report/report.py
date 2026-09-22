import boto3
ec2=boto3.client("ec2")
for s in ec2.describe_subnets()["Subnets"]:
 print(s["SubnetId"],s["VpcId"],s["AvailabilityZone"],s["CidrBlock"],s["AvailableIpAddressCount"])