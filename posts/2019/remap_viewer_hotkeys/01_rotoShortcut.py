def rotoShortcut():
	viewerMenu = nuke.menu('Viewer')
	viewerMenu.addCommand('Next Frame', "nuke.activeViewer().frameControl(+1)", 'w')
	viewerMenu.addCommand('Previous Frame', "nuke.activeViewer().frameControl(-1)", 'q')
	viewerMenu.addCommand('Next Keyframe', "nuke.activeViewer().frameControl(2)", 'alt+w')
	viewerMenu.addCommand('Previous Keyframe', "nuke.activeViewer().frameControl(-2)", 'alt+q')

	if nuke.thisNode().shown():
	    viewerMenu.findItem('Overlay').setEnabled(False)
	    viewerMenu.findItem('Enable Wipe').setEnabled(False)
	    viewerMenu.findItem('Set New ROI').setEnabled(False)
	    viewerMenu.findItem('Next Frame').setEnabled(True)
	    viewerMenu.findItem('Previous Frame').setEnabled(True)
	    viewerMenu.findItem('Next Keyframe').setEnabled(True)
	    viewerMenu.findItem('Previous Keyframe').setEnabled(True)
	else:
	    viewerMenu.findItem('Next Keyframe').setEnabled(False)
	    viewerMenu.findItem('Previous Keyframe').setEnabled(False)
	    viewerMenu.findItem('Next Frame').setEnabled(False)
	    viewerMenu.findItem('Previous Frame').setEnabled(False)
	    viewerMenu.findItem('Overlay').setEnabled(True)
	    viewerMenu.findItem('Enable Wipe').setEnabled(True)
	    viewerMenu.findItem('Set New ROI').setEnabled(True)

nuke.addKnobChanged(rotoShortcut, nodeClass='Roto')