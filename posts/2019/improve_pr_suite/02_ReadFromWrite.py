def read_from_write():
    """
    Create Read node from selected Write node.
    :return: None
    :rtype: None
    """
    selected = nuke.selectedNodes()
    writeNodes = []
    for node in selected:
        if node.Class() == 'Write':
            writeNodes.append(node)
        else:
            hasWrite = False
            for inNode in nuke.allNodes(group=node):
                if inNode.Class() == 'Write':
                    hasWrite = True
            if hasWrite:
                writeNodes.append(node)

    if len(writeNodes) < 1:
        nuke.message("Please select a Write node.")
    else:
        writeList = []
        for n in writeNodes:
            writeValues = []
            if n.Class() == 'Write':
                writeValues.append(n)
                writeValues.append(n.xpos())
                writeValues.append(n.ypos())
                writeList.append(writeValues)
            else:
                for inGroup in nuke.allNodes(group=n):
                    if inGroup.Class() == 'Write':
                        writeValues.append(inGroup)
                        writeValues.append(n.xpos())
                        writeValues.append(n.ypos())
                        writeList.append(writeValues)

        for write in writeList:
            if write[0]["use_limit"].value() is True:
                first_frame = write[0]["first"].value()
                last_frame = write[0]["last"].value()
            else:
                first_frame = nuke.Root()["first_frame"].value()
                last_frame = nuke.Root()["last_frame"].value()

            writeNode = nuke.nodes.Read(
                file=nuke.filename(write[0]),
                first=first_frame,
                last=last_frame,
                origfirst=nuke.Root()["first_frame"].value(),
                origlast=nuke.Root()["last_frame"].value())
            writeNode.setXpos(write[1]+100)
            writeNode.setYpos(write[2])