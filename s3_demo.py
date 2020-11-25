import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAYZJUXZC4CHEGNNZF'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'spencer.file.sync'

s3 = boto3.resource(
    service_name='s3',
    region_name='us-west-1',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
for bucket in s3.buckets.all():
    print(bucket.name)

for obj in s3.Bucket(BUCKET_NAME).objects.all():
    print(obj)

spencer = s3.Bucket(BUCKET_NAME)
spencer.download_file("static",  "./scene2.png")

print ("Done")