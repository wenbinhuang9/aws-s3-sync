import unittest

from key_val_text_parser import KVTestParser
class TestKeyValParser(unittest.TestCase):


    def test_parser(self):
        fileName = "./test_config"
        kvDb = KVTestParser(fileName)

        kvDb.set("access_key", "123213")
        kvDb.set("access_secretes", "312312")


        lines = None
        with open(fileName) as f:
            lines = f.readlines()

        correctList = ["access_key=123213\n", "access_secretes=312312\n"]
        self.assertListEqual(lines, correctList)

if __name__ == "__main__":

    unittest.main()
