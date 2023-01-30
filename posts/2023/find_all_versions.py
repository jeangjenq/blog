import re
from glob import glob

def detect_all_versions(path):
    # detect all versions that exists in node folder
    # nukescripts.version_latest() contains similar function
    # but it's only friendly with v+1
    # so if there's a version skip it stops at a certain version
    # not my prefer method
    versions = []
    # regex patterns to replace versions and frame paddings to *
    # we will use glob later to search for all files
    versions_pattern = [r"v-?\d+"]
    frame_paddings = [r"%\d+[dD]", r"\#+"]

    for pattern in versions_pattern + frame_paddings:
        path = re.sub(pattern, "*", path)
    
    # make sure all v### found in files are the same number
    # don't know under what occasion you might have 2 different versions
    # in same path, don't know what to do about it
    def all_same(items):
        return all(x == items[0] for x in items)
    # glob returns list of files that matches the pattern
    # in this case probably all the individual frames
    files = glob(path)
    versions = []
    for path in files:
        find_version = re.findall(versions_pattern[0], path)
        if find_version and all_same(find_version):
            if find_version[0] not in versions:
                versions.append(find_version[0])
    return versions