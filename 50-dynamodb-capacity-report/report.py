import os,boto3
d=boto3.client("dynamodb"); r=d.describe_table(TableName=os.environ["TABLE_NAME"])["Table"]
print("Table:",r["TableName"],"Status:",r["TableStatus"],"ItemCount:",r.get("ItemCount"))
print("Billing:",r["BillingModeSummary"].get("BillingMode") if r.get("BillingModeSummary") else "PROVISIONED")