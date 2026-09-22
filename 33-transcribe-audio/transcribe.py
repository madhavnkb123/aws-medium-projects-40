import os,time,boto3
tr=boto3.client("transcribe"); name="medium-demo-"+str(int(time.time()))
tr.start_transcription_job(TranscriptionJobName=name,Media={"MediaFileUri":os.environ["MEDIA_URI"]},MediaFormat=os.environ.get("FORMAT","mp3"),LanguageCode=os.environ.get("LANGUAGE","en-US"))
while True:
    j=tr.get_transcription_job(TranscriptionJobName=name)["TranscriptionJob"]; s=j["TranscriptionJobStatus"]
    if s in ("COMPLETED","FAILED"): break
    time.sleep(5)
print(s)
if s=="COMPLETED": print(j["Transcript"]["TranscriptFileUri"])