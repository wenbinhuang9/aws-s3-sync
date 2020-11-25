
import s3_proxy
import os 
import unittest

class TestS3Proxy(unittest.TestCase):
    def test_sync_file_command(self):
        filename = "./s3_demo"
        command = s3_proxy.genSyncFileCommand(filename)

        template = "aws s3 cp {0} s3://spencer.file.sync/{1}"
        result = template.format(filename, filename[2:])
        print(command)
        self.assertEqual(command, result)

        filename = "s3_demo"

        result = template.format(filename, filename)
        command = s3_proxy.genSyncFileCommand(filename)
        print(command)
        self.assertEqual(result, command)


        filename = "./image/scene1.png"

        result = template.format(filename, filename[2:])
        command = s3_proxy.genSyncFileCommand(filename)
        print(command)
        self.assertEqual(result, command)

    def test_sync_dir_command(self):
        dir = "./image"
        template = "aws s3 sync {0} s3://spencer.file.sync/{1}"

        result = template.format(dir, dir[2:])

        command = s3_proxy.genDirFileCommand(dir)

        print(command)

        self.assertEqual(command, result)
    
    def test_rm_filename_command(self):
        rmFilename = "./image/scene1.png"

        template = "aws s3 rm  s3://spencer.file.sync/{0}"

        result = template.format(rmFilename[2:])

        command = s3_proxy.genrmCommand(rmFilename)
        print("rm file command is:" + command)
        self.assertEqual(result, command)

    def test_sync_file_and_rm_file(self):
        dir = "./testfile"

        s3_proxy.sync(dir)

        with os.popen("aws s3 ls spencer.file.sync/testfile/") as f :
            result = f.read()

            print(result)
            self.assertTrue("hello.txt"  in result) 
            self.assertTrue("world.txt" in result)

        filename = "./testfile/hello.txt"

        s3_proxy.rm(filename)
        with os.popen("aws s3 ls spencer.file.sync/testfile/") as f :
            result = f.read()

            print(result)
            self.assertTrue("hello.txt" not in result)

        s3_proxy.sync(filename)
        
        with os.popen("aws s3 ls spencer.file.sync/testfile/") as f :
            result = f.read()

            print(result)
            self.assertTrue("hello.txt" in result)


    def test_sync_from_s3(self):
        dir = "./"

        correctCommand = "aws s3 sync s3://spencer.file.sync ./"
        returnCommand = s3_proxy.genSyncDirFromS3Command(dir)

        self.assertEqual(correctCommand, returnCommand)

if __name__ == '__main__':
    unittest.main()
