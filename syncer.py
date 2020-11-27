import sys 
import os 
import azure_blob_proxy
import s3_proxy
import google_drive_proxy 

SUPPORTED_CLOUD = ["s3", "az", "gd"]

def copyFromCloud(cloud, dir):
    if cloud not in SUPPORTED_CLOUD:
        raise Exception("unsupported cloud")

    if cloud == "s3":
        s3_proxy.syncDirFromS3(dir) 
    elif cloud == "az":
        azure_blob_proxy.syncDirFromS3(dir) 
    else:
        raise Exception("unsupported cloud")
 
def copyToCloud(cloud, dir):
    if cloud not in SUPPORTED_CLOUD:
        raise Exception("unsupported cloud")

    if cloud == "s3":
        s3_proxy.sync(dir) 
    elif cloud == "az":
        azure_blob_proxy.sync(dir)
    else:
        raise Exception("unsupported cloud")
    
    

def rm(cloud, file):
    if cloud not in SUPPORTED_CLOUD:
        raise Exception("unsupported cloud")

    if cloud == "s3":
        s3_proxy.rm(file) 
    elif cloud == "az":
        azure_blob_proxy.rm(file)

    else:
        raise Exception("unsupported cloud")


def cp(source, dest):
    if source in SUPPORTED_CLOUD:
        copyFromCloud(source, dest)
    else:
        
        copyToCloud(dest, source)
 
## todo implement it here 
def ls(cloud):
    if cloud not in SUPPORTED_CLOUD:
        raise Exception("unsupported cloud")

    if cloud == "s3":
        result = s3_proxy.ls()
        print(result)
    elif cloud == "az":
        result = azure_blob_proxy.ls()
        print(result)
    elif cloud == "gd":
        result = google_drive_proxy.ls()
    else:
        raise Exception("unsupported cloud")


## exmaple 
## input: s3/image  output: (s3, image)
## input: s3  output: (s3, ./)
def parseCloudDirectory(cloudDir):
    if cloudDir in SUPPORTED_CLOUD:
        cloud = cloudDir
        return (cloud, "./")
    
    splittedArr = cloudDir.split("/")

    cloud = splittedArr[0]
    dir = "/".join(splittedArr[1:])
    
    return (cloud, dir)

def main(argv):
    command = argv[1]

    if command == "cp":
        if len(argv) < 4:
            raise Exception("too less arugments for cp command")
        cp(argv[2], argv[3])
    elif command == "rm":
        ## syncer rm s3/image
        ## syncer rm az/image
        if len(argv) < 3:
            raise Exception("too less arguments for rm command")
        cloudDir = argv[2]
        cloud, dir = parseCloudDirectory(cloudDir)

        rm(cloud, dir)
    elif command == "ls":
        cloud = argv[2]
        ls(cloud)

    else:
        raise Exception("unsupported command")
    return



if __name__ == "__main__":

    if len(sys.argv) <= 1:
        raise Exception("please input valid command")

    main(sys.argv)
