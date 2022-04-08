import os

l = []
for root, directories, filenames in os.walk('E:\Onedrive'):
    for directory in directories:
        l.append(os.path.join(root, directory))
    for filename in filenames:
        l.append(os.path.join(root, filename))

for a in l:
    args = 'fsutil reparsepoint delete "' + a + '"'
    os.popen(args)