import boto3
ec2=boto3.client("ec2")
for rt in ec2.describe_route_tables()["RouteTables"]:
 print("ROUTE TABLE",rt["RouteTableId"],"VPC",rt["VpcId"])
 for r in rt["Routes"]: print(" ",r.get("DestinationCidrBlock"),r.get("GatewayId") or r.get("NatGatewayId"))