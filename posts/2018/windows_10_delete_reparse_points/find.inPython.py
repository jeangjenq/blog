l = []
for root, directories, filenames in os.walk('./'):
    for directory in directories:
        l.append(os.path.join(root, directory))
    for filename in filenames:
        l.append(os.path.join(root, filename))