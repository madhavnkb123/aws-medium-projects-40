import boto3
for x in boto3.client("ec2").describe_vpc_endpoints()["VpcEndpoints"]:
 print(x["VpcEndpointId"],x["VpcId"],x["VpcEndpointType"],x["ServiceName"],x["State"])