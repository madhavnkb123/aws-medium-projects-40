from datetime import date,timedelta
import boto3
end=date.today(); start=end-timedelta(days=30)
r=boto3.client("ce").get_cost_and_usage(TimePeriod={"Start":start.isoformat(),"End":end.isoformat()},Granularity="MONTHLY",Metrics=["UnblendedCost"],GroupBy=[{"Type":"DIMENSION","Key":"SERVICE"}])
for p in r["ResultsByTime"]:
    for g in p["Groups"]: print(g["Keys"][0],g["Metrics"]["UnblendedCost"]["Amount"])