import boto3
for g in boto3.client("autoscaling").describe_auto_scaling_groups()["AutoScalingGroups"]:
 print(g["AutoScalingGroupName"],g["MinSize"],g["DesiredCapacity"],g["MaxSize"],len(g["Instances"]))