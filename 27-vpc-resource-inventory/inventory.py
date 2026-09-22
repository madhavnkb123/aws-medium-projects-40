import boto3
ec2=boto3.client("ec2")
for v in ec2.describe_vpcs()["Vpcs"]: print("VPC",v["VpcId"],v.get("CidrBlock"),v.get("IsDefault"))
for s in ec2.describe_subnets()["Subnets"]: print("SUBNET",s["SubnetId"],s["VpcId"],s["CidrBlock"],s["AvailabilityZone"])
for n in ec2.describe_nat_gateways()["NatGateways"]: print("NAT",n["NatGatewayId"],n["State"],n["VpcId"])