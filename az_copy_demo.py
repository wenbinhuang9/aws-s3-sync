
import os 



command = "azcopy login --tenant-id=19a46ac2-a14b-4dfa-bce3-93965c21f4cf"

with os.popen(command) as f:

    print(f.read())

