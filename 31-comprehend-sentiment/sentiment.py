import os,boto3
text=os.environ.get("TEXT","AWS is useful for scalable applications.")
r=boto3.client("comprehend").detect_sentiment(Text=text,LanguageCode=os.environ.get("LANGUAGE","en"))
print(r["Sentiment"],r["SentimentScore"])