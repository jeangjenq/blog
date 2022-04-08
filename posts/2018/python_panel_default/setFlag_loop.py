def selectNodesPanel():
    p = nukescripts.PythonPanel('Conform file paths to Project Directory')
    p.nodesSelection = newUserKnob(nuke.Enumeration_Knob('nodesSel', 'Nodes selections', ['All nodes', 'Selected nodes only', 'Exclude selected nodes']), 2)
    p.checkReadGeo = newUserKnob(nuke.Boolean_Knob('checkReadGeo', 'Exclude ReadGeo nodes', '0'), 0)
    p.readGeoText = nuke.Text_Knob('readGeoText', '', 'Will affect configured scenegraph')
    for k in (p.nodesSelection, p.checkReadGeo, p.readGeoText):
        k.setFlag(0x1000)
        p.addKnob(k)