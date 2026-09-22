import boto3,datetime
iam=boto3.client("iam")
for u in iam.list_users()["Users"]:
    for k in iam.list_access_keys(UserName=u["UserName"])["AccessKeyMetadata"]:
        last=iam.get_access_key_last_used(AccessKeyId=k["AccessKeyId"]).get("AccessKeyLastUsed",{})
        age=(datetime.datetime.now(datetime.timezone.utc)-k["CreateDate"]).days
        print(u["UserName"],k["AccessKeyId"],k["Status"],"age_days",age,"last_used",last.get("LastUsedDate","never"))