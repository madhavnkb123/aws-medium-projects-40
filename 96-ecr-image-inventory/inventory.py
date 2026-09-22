import os,boto3
e=boto3.client("ecr")
for x in e.describe_images(repositoryName=os.environ["REPOSITORY"])["imageDetails"]:
 print(x.get("imageTags"),x.get("imagePushedAt"),x.get("imageSizeInBytes"))