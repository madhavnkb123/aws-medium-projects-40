import boto3
elbv2=boto3.client("elbv2")
for x in elbv2.describe_load_balancers()["LoadBalancers"]:
 print(x["LoadBalancerName"],x["Type"],x["Scheme"],x["DNSName"])