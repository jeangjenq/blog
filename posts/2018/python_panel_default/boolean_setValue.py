def newUserKnob(knob, value):
    knob.setValue(value)
    return knob

def selectNodesPanel():
    p = nukescripts.PythonPanel('Conform file paths to Project Directory')
    p.checkReadGeo = newUserKnob(nuke.Boolean_Knob('checkReadGeo', 'Exclude ReadGeo nodes', '0'), 0)