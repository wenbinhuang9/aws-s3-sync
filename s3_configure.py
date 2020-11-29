import os 

from key_val_text_parser import KVTestParser

CONG_FILE_NAME = "~/.syncer/s3_config"

AWS_S3_BUCKET_CONST = "aws_s3_bucket"


config_dir = "./.syncer"
configfile = os.path.join(config_dir, "s3_config")
def set(key, value):
    if not os.path.exists(config_dir):
        os.mkdir(config_dir)
    kvParser = KVTestParser(configfile)

    if value != "" and key != "":
        kvParser.set(key, value) 

def getBucket():
    kvParser = KVTestParser(configfile)

    return kvParser.get(AWS_S3_BUCKET_CONST)



    

