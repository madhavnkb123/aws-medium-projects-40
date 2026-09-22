import os,boto3
with open(os.environ["IMAGE"],"rb") as f: data=f.read()
r=boto3.client("rekognition").detect_labels(Image={"Bytes":data},MaxLabels=10,MinConfidence=80)
for x in r["Labels"]: print(x["Name"],round(x["Confidence"],2))