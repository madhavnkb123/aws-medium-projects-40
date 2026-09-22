import os,boto3,base64
kms=boto3.client("kms")
r=kms.encrypt(KeyId=os.environ["KMS_KEY_ID"],Plaintext=os.environ.get("TEXT","confidential").encode())
print("Ciphertext bytes:",len(r["CiphertextBlob"]))
d=kms.decrypt(CiphertextBlob=r["CiphertextBlob"])["Plaintext"]
print("Decrypted:",d.decode())