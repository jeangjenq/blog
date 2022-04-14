n = nuke.thisNode()
oValue = n['file'].evaluate()
if os.path.isfile(oValue):
    (prefix, v) = nukescripts.version_get(oValue, 'v')
    v = int(v) n['file'].setValue(nukescripts.version_set(n['file'].value(), prefix, v, v + 1))