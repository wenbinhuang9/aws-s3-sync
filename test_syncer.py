
import os 
import unittest

import syncer

BASE_URL = "https://spencer2.blob.core.windows.net/spencer-file-sync"
SAS = azure_blob_proxy.SAS

class TestSyncer(unittest.TestCase):
    def ls_az(self):
        command = "azcopy list '{0}/{1}'".format(BASE_URL, SAS)
        with os.popen(command) as f:
            return f.read()
        
        return ""

    def ls_s3():
        with os.popen("aws s3 ls spencer.file.sync/testfile") as f :
            result = f.read()
            return result
        
    def test_parse_cloud_dir(self):
        cloudDir = "s3"
        cloud, dir = syncer.parseCloudDirectory(cloudDir) 

        self.assertTrue(cloud == "s3")
        self.assertTrue(dir == "./")

        cloudDir = "s3/image"
        cloud, dir = syncer.parseCloudDirectory(cloudDir) 

        self.assertTrue(cloud == "s3")
        self.assertTrue(dir == "image")

    def test_cp_to_cloud(self):
        cloud = "az"
        dir = "./testfile"
        syncer.copyToCloud(cloud, dir)

        azList = self.ls_az()

        shouldInlcude = ["testfile/hello.txt", "testfile/world.txt", "testfile/src/hello.txt", "testfile/src/world.txt"]

        self.assertTrue(all((iterm in azList) for iterm in shouldInlcude))

        cloud = "s3"
        dir = "./testfile"
        syncer.copyToCloud(cloud, dir)
        s3List =self.ls_s3()
        self.assertTrue(all((iterm in s3List) for iterm in shouldInlcude))


if __name__ == '__main__':
    unittest.main()
