import os 
from os import path

class KVTestParser():
    def __init__(self, filename):
        self.filename = filename
        self.kvDict = {}

        self._read()

    def get(self, key ):
        return self.kvDict[key] 

    def set(self, key, value):
        self.kvDict[key] = value
        self._persistence()


    def _read(self):
        with open (self.filename, "w+") as f:
            lines = f.readlines() 
            for line in lines:
                line_splitted = line.split("=")
                key, value = line_splitted[0].strip(), line_splitted[1].strip()

                self.kvDict[key] = value
    def _persistence(self):
        with open(self.filename, "w") as f :
            lines = []
            for k, v in self.kvDict.items():
                line = ("=".join([k, v]) + "\n")
                lines.append(line)
            
            f.writelines(lines)
        
