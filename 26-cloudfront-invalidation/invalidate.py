import os,time,boto3
paths=[x.strip() for x in os.environ.get("PATHS","/*").split(",") if x.strip()]
r=boto3.client("cloudfront").create_invalidation(DistributionId=os.environ["DISTRIBUTION_ID"],InvalidationBatch={"Paths":{"Quantity":len(paths),"Items":paths},"CallerReference":os.environ.get("CALLER_REFERENCE",str(time.time()))})
print(r["Invalidation"]["Id"],r["Invalidation"]["Status"])