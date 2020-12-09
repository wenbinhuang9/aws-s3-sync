
# Syncer:  A Tool for File BackUp Leveraging Multiple Cloud Storages

Group Member: Wenbin Huang

NetID: vx3255

Course: CS623 Cloud Computing 

Source Code in Github: https://github.com/wenbinhuang9/syncer

# Introduction 

Document backup is very important because storage hardwares , such as disk, HDD, SSD, has a potential risk of corruption. Traditionally, we usually buy disk drive for backup, so we have to maintain hardwares, which is costly and time consuming. Currently, we can leverage multiple cloud storages to enable backup without maintaining the hardware. Further, backup on the cloud is safe, cheap and also easy. So, in this project, I will leverage Azure Blob Storage, AWS S3 and Google Drive to provide unified interfaces to access back up service on cloud. 

# Architecture, Orchestration Model And Flow Diagram
 
## Architecture 

![](image/Screen%20Shot%202020-11-28%20at%207.48.22%20PM.png)

The above picture is the layered architecture of my project. There are three modules Proxy, Authentation and Commandline Interface. 

### Commandline Interface

The project provides unified APIs to access multiple cloud storages to reduce learning curve and complexity. The APIs is easy to use because it is compatible with Linux File System Commandline. The following is examples of API, which copys local file to different clouds. 

```shell
syncer cp ./hello.txt s3
syncer cp ./hello.txt gdrive
syncer cp ./hello.txt az
```

### Proxy 

Proxy encapsulates functionality from different cloud storages, providing unified APIs for Commandline Interface Module to access.

### Authentication 

Each cloud has its own authentication way, so I have to encapsulates Authentication Module to provide unified APIs for Commandline Interface Module to authenticate different cloud storages. 

## Orchestration Model 


## Flow Diagram

![](image/archestration_model_small.png)

The above picture is the Orchestration Model to use Syncer tool, we just need to authenticate the cloud storage in advance, and then we can use 


# Source Code 

Project is managed by the github, check the following link to view the code. 

Github: https://github.com/wenbinhuang9/syncer

# Database Model and Diagram



# Clouds and Technologies Used 

## Cloud used 
1. AWS S3 and IAM 
2. Azure Blob Storage and IAM
3. Google Drive and IAM 
   
## Programming Languages 

- Python 3.0 and Python Unittest Framework

## Libraries Used 
1. **AWS CLI** to access  S3 
2. **Azure azcopy CLI** to access Azure Blob Storage
3. **PyDrive API** to access Google Drive  

# CommandLine Interfaces 

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

# Environment Required and Deployment 

## Environment and Libraries Required
- OS: OSX(Apple MAC)
- Python3.0 
- 


## Deployment 

## Authentication Configuration 


# Conclusion 

In this project , I have provided a simple API to back up local file to cloud storage. The future direction is to provide flexible authentication, to support more cloud storages and also to consider encryption for security. 
