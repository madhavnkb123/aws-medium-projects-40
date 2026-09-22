import os,boto3
ec2=boto3.client("ec2"); ids=[x.strip() for x in os.environ.get("INSTANCE_IDS","").split(",") if x.strip()]; action=os.environ.get("ACTION","stop")
if not ids: raise SystemExit("Set INSTANCE_IDS")
if action=="start": print(ec2.start_instances(InstanceIds=ids)["StartingInstances"])
elif action=="stop": print(ec2.stop_instances(InstanceIds=ids)["StoppingInstances"])
else: raise SystemExit("ACTION must be start or stop")