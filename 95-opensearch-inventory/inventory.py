import boto3
for x in boto3.client("opensearch").list_domain_names()["DomainNames"]:
 print(x["DomainName"])