import boto3
import os
from botocore.exceptions import NoCredentialsError
from uuid import uuid4

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

def upload_file_to_s3(file_obj, filename, content_type):
    key = f"media/{uuid4()}_{filename}"
    try:
        s3_client.upload_fileobj(
            Fileobj=file_obj,
            Bucket=BUCKET_NAME,
            Key=key,
            ExtraArgs={"ContentType": content_type, "ACL": "public-read"}
        )
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{key}"
        return file_url
    except NoCredentialsError:
        raise Exception("AWS credentials not found")

