import os 
from os import path
from key_val_text_parser import KVTestParser


BUCKETNAME = 'spencer.file.sync'

def ls():
    with os.popen("aws s3 ls {0}".format(BUCKETNAME)) as f :
        result = f.read()
        return result

    return ""

def sync(filename):
    if path.isfile(filename):
        _syncFile(filename)
    else:
        _syncDir(filename)

def preprocessingTargetFileName(fileName):
    target = fileName
    if fileName.startswith("./"): 
        target =  fileName[2:]

    return "s3://{0}/{1}".format(BUCKETNAME, target) 


def genSyncFileCommand(filename):
    target = preprocessingTargetFileName(filename)
    command = "aws s3 cp {0} {1}".format(filename, target) 

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
    
    command  = "aws s3 sync {0} s3://{1}/{2}".format(dir, BUCKETNAME, target)

    return command 

def _syncDir(dir):
    command = genDirFileCommand(dir)

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
        _rmFile(filename, True)
        return
    
    _rmFile(filename, False)
 
def genrmCommand(filename, isRecursive):
    target = preprocessingTargetFileName(filename)

    command = "aws s3 rm  {0}".format(target)

    if isRecursive:
        command += " --recursive"
    return command 

def _rmFile(filename, isRecursive):
    command = genrmCommand(filename, isRecursive)

    executeCommand(command)


