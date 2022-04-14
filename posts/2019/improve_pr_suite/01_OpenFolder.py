def open_folder(path):
    """
    Open folder based on OS.
    :param path: Directory path
    :type path: str
    :return: None
    :rtype: None
    """
    if platform.system() == "Windows":
        os.startfile(os.path.abspath(path))
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    elif platform.system() == "Linux":
        subprocess.check_call(["xdg-open", path])
    else:
        nuke.message("Unsupported OS")
 
 
def open_read_file():
    """
    Open folder for selected node with file knob.
    :return: None
    :rtype: None
    """
    read_path = []
    for node in nuke.selectedNodes():
        for knob in node.knobs():
            current_knob = node[knob]
            if current_knob.Class() == 'File_Knob':
                if current_knob.evaluate() is not None:
                    if os.path.dirname(current_knob.evaluate()) not in read_path:
                        read_path.append(os.path.dirname(current_knob.evaluate()))
    if len(read_path) > 4:
        if nuke.ask('About to open ' + str(len(read_path)) + " paths, continue?"):
            for path in read_path:
                open_folder(path)
    else:
        for path in read_path:
            open_folder(path)