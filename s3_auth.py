import os 

import subprocess, shlex
import s3_configure
AWS_ACCESS_KEY_ID_CONST = "aws_access_key_id"
AWS_SECRET_ACCESS_KEY_CONST = "aws_secret_access_key"
AWS_S3_BUCKET_CONST = "aws_s3_bucket"

def auth():
    aws_access_key_id = input("AWS Access Key ID = ")
    
    aws_secret_access_key = input("AWS Secret Access Key = ")

    s3_bucket = input("S3 Bucket = ")

    if aws_access_key_id.strip() != "":
        _update_to_aws_configuration(AWS_ACCESS_KEY_ID_CONST, aws_access_key_id)
    if aws_secret_access_key.strip() != "":
        _update_to_aws_configuration(AWS_SECRET_ACCESS_KEY_CONST, aws_secret_access_key)
    if s3_bucket.strip() != "":
        s3_configure.set(s3_configure.AWS_S3_BUCKET_CONST, s3_bucket)

    print("Login Completed")

def _update_to_aws_configuration(key, value):
    command = "aws configure set {0} {1}".format(key, value)
    with os.popen(command) as f :
        pass 


    
