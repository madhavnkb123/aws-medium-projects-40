import os,boto3
with open(os.environ["FILE"],"rb") as f: data=f.read()
r=boto3.client("textract").detect_document_text(Document={"Bytes":data})
for b in r["Blocks"]:
    if b["BlockType"]=="LINE": print(b["Text"])