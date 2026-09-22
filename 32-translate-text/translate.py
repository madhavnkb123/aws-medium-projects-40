import os,boto3
r=boto3.client("translate").translate_text(Text=os.environ["TEXT"],SourceLanguageCode=os.environ.get("SOURCE","en"),TargetLanguageCode=os.environ.get("TARGET","hi"))
print(r["TranslatedText"])