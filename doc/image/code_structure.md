
```mermaid
graph LR;
    S[syncer.py]-->Proxy;
    S-->Authentcation;
    Authentcation-->google_drive_auth.py 
    Authentcation-->s3_auth.py
    Authentcation-->azure_auth.py
    Proxy-->google_drive_proxy.py;
    Proxy-->azure_blob_proxy.py
    Proxy-->s3_proxy.py
```