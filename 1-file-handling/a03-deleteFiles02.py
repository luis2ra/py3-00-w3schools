'''

Check if File exist

To avoid getting an error, you might want to check if the file exists before you try to delete it.

'''

import os
if os.path.exists("files/demofile.txt"):
    os.remove("files/demofile.txt")
else:
    print("The file does not exist")