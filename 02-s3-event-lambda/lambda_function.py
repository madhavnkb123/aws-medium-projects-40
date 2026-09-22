import urllib.parse
def lambda_handler(event,context):
    for r in event.get("Records",[]):
        b=r["s3"]["bucket"]["name"]; k=urllib.parse.unquote_plus(r["s3"]["object"]["key"])
        print(f"S3 event: s3://{b}/{k}")
    return {"statusCode":200,"records":len(event.get("Records",[]))}