import boto3
for n in boto3.client("ec2").describe_nat_gateways()["NatGateways"]:
 print(n["NatGatewayId"],n["State"],n["VpcId"],n.get("CreateTime"))