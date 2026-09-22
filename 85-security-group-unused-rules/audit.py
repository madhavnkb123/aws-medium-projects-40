import boto3
ec2=boto3.client("ec2")
for sg in ec2.describe_security_groups()["SecurityGroups"]:
 for p in sg["IpPermissions"]:
  if any(x.get("CidrIp")=="0.0.0.0/0" for x in p.get("IpRanges",[])): print("Review public rule:",sg["GroupId"],p.get("FromPort"),p.get("ToPort"))