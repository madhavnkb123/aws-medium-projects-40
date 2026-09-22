import os,boto3
ec2=boto3.client("ec2")
for vid in [x.strip() for x in os.environ.get("VOLUME_IDS","").split(",") if x.strip()]:
    r=ec2.create_snapshot(VolumeId=vid,Description=f"Automated snapshot of {vid}")
    ec2.create_tags(Resources=[r["SnapshotId"]],Tags=[{"Key":"CreatedBy","Value":"aws-medium-projects-40"}])
    print(r["SnapshotId"])