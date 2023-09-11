import boto3
import botocore
import uuid
import os
from .config import Config
s3_client = boto3.client("s3", aws_access_key_id=os.environ.get("AWS_AK"), aws_secret_access_key=os.environ.get("AWS_SK"))



def allowed_file(filename):
    print(filename)
    print(filename.rsplit(".",1)[1].lower())
    return "." in filename and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def get_unique_filename(filename):
    ext = filename.rsplit(".", 1)[1].lower()
    unique_filename= uuid.uuid4().hex
    return f"{unique_filename}.{ext}"

def upload_file_to_s3(s3client, bucket, file):
    try:
        print("S3 CLIENT")
        print(type(s3client))
        print("BUCKET")
        print(type(bucket))
        print("FILE")
        print(type(file))
        s3client.upload_fileobj(
            file,
            bucket,
            file.filename,
            ExtraArgs={
                "ContentType": file.content_type
            }
        )
    except Exception as e:
        return {"errors":str(e)}
    s3location=f"https://{bucket}.s3.amazonaws.com"
    return {"url": f"{s3location}/{file.filename}"}