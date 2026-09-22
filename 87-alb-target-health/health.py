import os,boto3
elbv2=boto3.client("elbv2")
tg=os.environ["TARGET_GROUP_ARN"]
for x in elbv2.describe_target_health(TargetGroupArn=tg)["TargetHealthDescriptions"]:
 print(x["Target"]["Id"],x["TargetHealth"]["State"],x["TargetHealth"].get("Reason",""))