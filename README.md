# syncer

A tool for file backUp leveraging AWS S3, Azure Blob Storage and Google Drive. 

# How to use 

Authtication
```
syncer login gdrive
syncer login s3
syncer login az
```
List file list on cloud
```
syncer ls gdrive
syncer ls s3
syncer ls az
```
Backup a local directory or file to cloud 
```
syncer cp ./testfile gdrive
syncer cp ./hello.txt s3
syncer cp ./hello.txt az
```
Copy from cloud to local 
```
syncer cp s3/hello.txt ./
syncer cp gdrive/{fileid} ./
syncer cp az/world.txt ./
```
Delete a directory  
```
syncer rm gdrive/{fileid}
syncer rm s3/hello.txt
syncer rm az/world.txt 
```