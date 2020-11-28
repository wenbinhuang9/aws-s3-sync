import os 
from os import path

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import google_drive_auth
from os import walk

DRIVE = google_drive_auth.auth()

def ls():
    global DRIVE
    file_list = DRIVE.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    
    return ""

def create_folder(folder_name,parent_folder_id = ""):
    file_metadata = {
        'title':folder_name,
        'name' : folder_name,
        #   'parents' : [folder_id],
       'mimeType' : 'application/vnd.google-apps.folder'
    }
    if parent_folder_id != "":
      file_metadata = {
        'title':folder_name,
        'name' : folder_name,
        'parents' : [parent_folder_id],
       'mimeType' : 'application/vnd.google-apps.folder'
    }      

    file = DRIVE.CreateFile(file_metadata)

    result = file.Upload()



# output map, key is folder name, value is folder id
def queryFolder(folderId =""):

    queryId = folderId if folderId != "" else "root"

    ## todo make success here
    result = {}
    file_list =DRIVE.ListFile({'q': "'%s' in parents and trashed=false and mimeType='application/vnd.google-apps.folder'" % queryId}).GetList()
    for file1 in file_list:
        title = file1['title']
        id = file1['id']
        result[title] = id 

    return result 

# output map, key is folder name, value is folder id
def queryFileList(folderId =""):

    queryId = folderId if folderId != "" else "root"

    ## todo make success here
    result = {}
    file_list =DRIVE.ListFile({'q': "'%s' in parents and trashed=false" % queryId}).GetList()

    return file_list

def sync(source, destFolderId = ""):
    if path.isfile(source):
        _syncFile(source, destFolderId)
    else:
        _syncDir(source, destFolderId)

def preprocessingTargetFileName(fileName):
    target = fileName
    if fileName.startswith("./"): 
        target =  fileName[2:]

    return "s3://{0}/{1}".format(BUCKETNAME, target) 


def genSyncFileCommand(filename):
    target = preprocessingTargetFileName(filename)
    command = "aws s3 cp {0} {1}".format(filename, target) 

    return command

##exampel input: ./image/1.png , output: 1.png
def getFileName(filename):
    if "/" not in filename:
        return filename

    l = filename.split("/")

    return l[-1]
def _syncFile(filename, parentId = ""):
    if(DRIVE == None):
        authDrive()

    singleFileName = getFileName(filename)

    fileMetaData = {'title': singleFileName}

    if parentId != "":
        fileMetaData = {'title': singleFileName, 'parents' : [{"kind": "drive#fileLink","id": parentId}] }
    print(fileMetaData)
    file1 = DRIVE.CreateFile(fileMetaData)


    file1.SetContentFile(filename)
    file1.Upload()



def genDirFileCommand(dir):
    target = dir
    if dir == "." or dir == "./":
        target = ""
    elif dir.startswith("./"):
       target = dir[2:]  
    
    command  = "aws s3 sync {0} s3://{1}/{2}".format(dir, BUCKETNAME, target)

    return command 

def _getAllFileNames(dir):
    f = []
    for (dirpath, dirnames, filenames) in walk(dir):
        f.extend(filenames)

    return f

def getDirName(dir):
    if "/" not in dir :
        return dir

    dir_split = dir.split("/")
    if len(dir_split) > 2:
        raise Exception("unsupported two depth nested directory when using google drive")

    return dir_split[1]

def _syncDir(dir, destId=""):
    filenameList = _getAllFileNames(dir)
    if destId != "":
        for filename in filenameList:
            fullFilePath = dir + "/" + filename
            _syncFile(fullFilePath, destId)

        return

    clear_dir = getDirName(dir)

    gdriveDir = queryFolder()

    if clear_dir not in gdriveDir:
        create_folder(clear_dir)
        gdriveDir = queryFolder() 
    
    clearDirID = gdriveDir[clear_dir]
    if not clearDirID:
        raise Exception("can not get dir:%s id in google drive" % clear_dir)
    for filename in filenameList:
        fullFilePath = dir + "/" + filename
        _syncFile(fullFilePath, clearDirID)

def genSyncDirFromS3Command(dir):
    command = "aws s3 sync s3://{0} {1}".format(BUCKETNAME, dir)

    return command



## todo finish this part here 
def syncDirFromS3(source, dest):

    gfile = DRIVE.CreateFile({'id':source})
    gfile.FetchMetadata() 

    if isDir(gfile):
        if  not os.path.exists(dest):
            os.mkdir(dest)

        subFileList = queryFileList(source)
        for subFile in subFileList:
            title = subFile['title']
            curFileDest = os.path.join(dest, title)

            _syncFileFromCloud(subFile, curFileDest)
    else:
        _syncFileFromCloud(gfile, dest) 


def isDir(gfile):
    mimeType = gfile['mimeType']

    return mimeType == 'application/vnd.google-apps.folder'


def _syncFileFromCloud(gfile, dest):
    filename = gfile['title']
    if os.path.isdir(dest):
        dest = os.path.join(dest, filename)

    gfile.GetContentFile(dest)


def rm(fileId):
    file1 = DRIVE.CreateFile({'id': fileId})

    file1.Trash()

    print("rm done of id %s" % fileId)