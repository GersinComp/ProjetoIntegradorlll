import boto3
import os
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = 'recibos-projeto'    # os.getenv('S3_BUCKET')
S3_REGION = 'us-east-2'    # os.getenv('S3_REGION')
S3_ACCESS_KEY = 'AKIA6GBMFJPA2MBAIYV4'    # os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = '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'    # os.getenv('S3_SECRET_KEY')

if not all([S3_BUCKET, S3_REGION, S3_ACCESS_KEY, S3_SECRET_KEY]):
    raise EnvironmentError("Uma ou mais variáveis de ambiente AWS não foram carregadas corretamente.")

s3_client = boto3.client(
    's3',
    region_name=S3_REGION,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY
)


def upload_to_s3(file, filename):
    try:
        s3_client.upload_fileobj(file, S3_BUCKET, filename)
        print(f"File {filename} uploaded successfully")
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise e
