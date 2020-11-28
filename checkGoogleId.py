
import google_drive_auth

DRIVE = google_drive_auth.auth()


# output map, key is folder name, value is folder id
def queryFolder(fileId):
    result = {}
    file_list =DRIVE.ListFile({'q': "id='%s' and trashed=false" % fileId}).GetList()

    for file1 in file_list:
        title = file1['title']
        id = file1['id']
        result[title] = id 

        print(file1)
    return result 



id = "1543L0LAkspeqDVr-Q--1UNLfunatsRFk"

print(isDir(id))