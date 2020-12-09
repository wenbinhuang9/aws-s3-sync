
#  Design of file system sync to S3

## Cloud computing platform supported

- AWS S3
- Azure , what ? 
- Google Cloud Platform, what ? 

## Software and Library to be used 

boto3: a python SDK supporting s3 service access 



## Application 

### Back up of local file system 

### Building Static Website 

Make it easy to build a static website very simple

## Interface design

todo how to design interface here 
### sync to cloud 

### sync from cloud 

### rm in the cloud 


### Command line interface 

```shell
syncer login s3
syncer login az
```

```shell
syncer cp  ./ s3

syncer cp ./image az

syncer cp az  ./

syncer cp s3 ./ 
```
```
syncer rm  s3 ./image 
```
```
syncer ls s3

syncer ls azure 
```

```
syncer mkcon s3/S3_Container
syncer mkcon az/AZ_Container
```

## Reference document 

[azure blob storage interface](https://docs.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy-remove?toc=/azure/storage/blobs/toc.json)

[aws s3 interface ]()