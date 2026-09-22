import boto3
sensitive={22,3389,3306,5432}; ec2=boto3.client("ec2")
for sg in ec2.describe_security_groups()["SecurityGroups"]:
    for p in sg["IpPermissions"]:
        ports=range(p.get("FromPort",0),p.get("ToPort",p.get("FromPort",0))+1)
        world=any(x.get("CidrIp")=="0.0.0.0/0" for x in p.get("IpRanges",[]))
        if world and any(x in sensitive for x in ports): print("RISK",sg["GroupId"],sg["GroupName"],list(ports))