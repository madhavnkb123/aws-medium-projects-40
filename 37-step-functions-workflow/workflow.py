import os,json,boto3
r=boto3.client("stepfunctions").start_execution(stateMachineArn=os.environ["STATE_MACHINE_ARN"],input=json.dumps({"task":"demo","value":42}))
print("ExecutionArn:",r["executionArn"])