
```mermaid
graph TD;
    CommandLineInterface-->Proxy;
    CommandLineInterface-->Authentcation;
    Authentcation-->AWS_IAM 
    Authentcation-->AzureActiveDirectory;
    Authentcation-->GoogleDriveIAM
    Proxy-->S3;
    Proxy-->AzureBlobStorage
    Proxy-->GoogleDrive
```