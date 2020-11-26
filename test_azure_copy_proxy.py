
import azure_blob_proxy
import os 
import unittest

BASE_URL = "https://spencer2.blob.core.windows.net/spencer-file-sync"
SAS = azure_blob_proxy.SAS

class TestAzureBlogStorageProxy(unittest.TestCase):

    def ls(self):
        command = "azcopy list '{0}/{1}'".format(BASE_URL, SAS)
        with os.popen(command) as f:
            return f.read()
        
        return ""

    def test_sync_file_command(self):
        filename = "./world.txt"
        command = azure_blob_proxy.genSyncFileCommand(filename)

        correctCommand = "azcopy copy {0} 'https://spencer2.blob.core.windows.net/spencer-file-sync/world.txt{1}'"

        self.assertEqual(command, correctCommand.format(filename, SAS))


        filename = "world.txt"

        command = azure_blob_proxy.genSyncFileCommand(filename)
        print(command)
        self.assertEqual(command, correctCommand.format(filename, SAS))


        filename = "./src/world.txt"

        command = azure_blob_proxy.genSyncFileCommand(filename)
        
        correctCommand = "azcopy copy {0} 'https://spencer2.blob.core.windows.net/spencer-file-sync/src/world.txt{1}'"

        self.assertEqual(command, correctCommand.format(filename, SAS))

    def test_sync_dir_command(self):
        dir = "./image"
        template = "azcopy sync {0} 'https://spencer2.blob.core.windows.net/spencer-file-sync/{1}{2}'"

        correctResult = template.format(dir, dir[2:], SAS)

        command = azure_blob_proxy.genDirFileCommand(dir)
        print(command)
        self.assertEqual(command, correctResult)
    
    def test_rm_filename_command(self):
        rmFilename = "./image/scene1.png"

        
        template = "azcopy rm '{0}/{1}{2}'".format(BASE_URL, rmFilename[2:], SAS)

        command = azure_blob_proxy.genrmCommand(rmFilename)
        print("rm file command is:" + command)
        self.assertEqual(template, command)

    def test_sync_file_and_rm_file(self):
        
        ## todo test with rm file 


        dir = "./testfile"

        azure_blob_proxy.sync(dir)

        listResult = self.ls()

        shouldInlcude = ["testfile/hello.txt", "testfile/world.txt", "testfile/src/hello.txt", "testfile/src/world.txt"]

        self.assertTrue(all((iterm in listResult) for iterm in shouldInlcude))

        azure_blob_proxy.rm(dir)
        listResult = self.ls()
        self.assertTrue(all((iterm not in listResult) for iterm in shouldInlcude))
        
        filename = "./testfile/hello.txt"

        azure_blob_proxy.sync(filename)
        listResult = self.ls()
        shouldInlcude = ["testfile/hello.txt"]

        self.assertTrue(all((iterm in listResult) for iterm in shouldInlcude))
 

    # def test_sync_from_s3(self):
    #     dir = "./"

    #     correctCommand = "aws s3 sync s3://spencer.file.sync ./"
    #     returnCommand = azure_blob_proxy.genSyncDirFromS3Command(dir)

    #     self.assertEqual(correctCommand, returnCommand)

if __name__ == '__main__':
    unittest.main()
