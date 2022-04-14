opts = ('on', 'from auto-localize path', 'off')
p = nuke.Panel('Change read localization')
p.addEnumerationPulldown('Set localization policy', opts)