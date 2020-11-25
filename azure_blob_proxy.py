import os 
from os import path

STORAGE_NAME = 'spencer2'
BUCKETNAME = 'spencer-file-sync'

URL = "https://{0}.blob.core.windows.net/{1}".format(STORAGE_NAME, BUCKETNAME)

SAS = "?sv=2019-12-12&ss=b&srt=sco&sp=rwdlacx&se=2020-12-07T13:08:45Z&st=2020-11-25T05:08:45Z&spr=https,http&sig=m7pT%2FtnVL9rtq62oeANGGIygAQZVMYB6IzgW12%2F5kvw%3D"

def sync(filename):
    if path.isfile(filename):
        _syncFile(filename)
    else:
        _syncDir(filename)

def preprocessingTargetFileName(fileName):
    target = fileName
    if fileName.startswith("./"): 
        target =  fileName[2:]
    newURL = URL + "/" + target

    return newURL

def genSyncFileCommand(filename):
    target = preprocessingTargetFileName(filename)
    command = "azcopy copy {0} {1}{2}".format(filename, target, SAS) 

    return command


def _syncFile(filename):
    command = genSyncFileCommand(filename)

    executeCommand(command)

def genDirFileCommand(dir):
    target = dir
    if dir == "." or dir == "./":
        target = ""
    elif dir.startswith("./"):
       target = dir[2:]  
    
    source = dir
    dest = URL + "/" + target
    command  = "azcopy sync {0} {1}{2}".format(source, dest, SAS)

    return command 

def _syncDir(dir):
    command = genDirFileCommand(dir)
    print("azure sync dir command is {0}".format(command))
    executeCommand(command)

def genSyncDirFromS3Command(dir):
    command = "aws s3 sync s3://{0} {1}".format(BUCKETNAME, dir)

    return command

def syncDirFromS3(dir):
    command = genSyncDirFromS3Command(dir)
    executeCommand(command)


def executeCommand(command):
    with os.popen(command) as f:
        result = f.read()
        print(result)
    return

def rm(filename):
    if path.isdir(filename):
        print("does not support directory deletion")
        return
    
    _rmFile(filename)
 
def genrmCommand(filename):
    target = preprocessingTargetFileName(filename)

    command = "azcopy rm {0}{1}".format(target, SAS)

    return command 
def _rmFile(filename):
    command = genrmCommand(filename)

    executeCommand(command)


