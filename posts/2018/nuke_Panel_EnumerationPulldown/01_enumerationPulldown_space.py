opts = ('on', re.escape('from auto-localize path'), 'off')
reOpts = ','.join(opts)
policyOpts = reOpts.replace(',',' ')
p = nuke.Panel('Change read localization')
p.addEnumerationPulldown('Set localization policy', policyOpts)