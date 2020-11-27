import os 
from os import path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

BUCKETNAME = 'spencer.file.sync'


## todo my target is to authenticate only for once 
## todo how to do with google drive authentication??? 
gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

DRIVE = GoogleDrive(gauth)


def ls():
    global DRIVE

    file_list = DRIVE.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    
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
    if(DRIVE == None):
        authDrive()


    file1 = DRIVE.CreateFile({'title': filename})
    path = "./" + filename
    file1.SetContentFile(path)
    file1.Upload()



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


