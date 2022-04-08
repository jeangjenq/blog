import os
from subprocess import call

#gather a list of files/directories/subdirectories
list = []
for root, directories, filenames in os.environ['OneDrive']:
    for directory in directories:
        list.append(os.path.join(root, directory))
    for filename in filenames:
        list.append(os.path.join(root, filename))

#run 'fsutil reparsepoint delete #filename' for every thing in the list
for file in list:
    call(["fsutil", "reparsepoint", "delete", file])