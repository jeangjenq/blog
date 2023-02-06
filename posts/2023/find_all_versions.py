import re
from glob import glob

def detect_all_versions(self, node):
    '''
    detect all versions that exists in node folder
    nukescripts.version_latest() contains similar function
    but it's only friendly with v+1
    so if there's a version skip it stops at a certain version
    not my prefer method
    '''
    versions = []
    file = nuke.filename(node).replace('\\', '/')
    # regex patterns to replace versions and frame paddings to *
    # we will use glob later to search for all files
    versions_pattern = r"(?P<symbol>[\._\\/])(?P<prefix>[vV])(?P<num>-?\d+)"
    frame_paddings = [r"%\d+[dD]", r"\#+"]

    file = re.sub(versions_pattern, "\g<symbol>\g<prefix>[0-9]*", file)
    for pattern in frame_paddings:
        file = re.sub(pattern, "[0-9]*", file)
    # example of file at this point
    #  /media/checker_v[0-9]*/checker_v[0-9]*.[0-9]*.exr
    
    # glob  will returns list of files that matches the pattern
    # in this case probably all the individual frames
    files = glob(file)
    versions = []
    for file in files:
        find_version = re.search(versions_pattern, file)
        if find_version:
            version = find_version.group('prefix') + find_version.group('num')
            if version not in versions:
                versions.append(version)
    return versions