import os,boto3
r53=boto3.client("route53"); zone=os.environ["HOSTED_ZONE_ID"].rstrip("/")
for r in r53.list_resource_record_sets(HostedZoneId=zone)["ResourceRecordSets"]: print(r["Name"],r["Type"])
if os.environ.get("UPSERT")=="true":
    r53.change_resource_record_sets(HostedZoneId=zone,ChangeBatch={"Changes":[{"Action":"UPSERT","ResourceRecordSet":{"Name":os.environ["RECORD_NAME"],"Type":"A","TTL":300,"ResourceRecords":[{"Value":os.environ["RECORD_VALUE"]}]}}]})
    print("DNS record upserted")