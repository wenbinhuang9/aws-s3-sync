
```mermaid
graph TD;
    CommandLineInterface-->StorageProxy;
    CommandLineInterface-->Authentcation;
    Authentcation-->AWS_IAM 
    Authentcation-->Azure_Active_Directory;
    StorageProxy-->S3;
    StorageProxy-->Azure_Blob_Storage
```