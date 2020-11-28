import google_drive_auth

driver = google_drive_auth.auth()

## if parent_folder_id is "", just create folder under root direcotry  
def create_folder_in_folder(folder_name,parent_folder_id = ""):
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


    file = driver.CreateFile(file_metadata)

    print ('Folder ID: %s' % file.get('id'))
    print(file)

    result = file.Upload()
    print(result)


# output map, key is folder name, value is folder id
def queryFolder():

    file_list =driver.ListFile({'q': "'root' in parents and trashed=false and mimeType='application/vnd.google-apps.folder'"}).GetList()
    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
    
create_folder_in_folder("src", "1w9yk8yYMg5PZN7bvBnJO8glVFg9E5kwN")

queryFolder()


