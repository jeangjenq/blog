for layer in extract:
    shuffle = nuke.nodes.Shuffle(label='[value in]')
    shuffle["in"].setValue(layer)
    shuffle.setInput(0, self.node)