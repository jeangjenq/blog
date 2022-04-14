p.checkboxKnob = nuke.Boolean_Knob('readOnly', 'Read nodes only', '1')
p.localizationKnob = nuke.Enumeration_Knob('localizationPol', 'Set localization policy', ['on', 'from auto-localize path', 'on demand', 'off'])
p.textKnob = nuke.Text_Knob('text', '', '"on demand" only available since nuke11.1')