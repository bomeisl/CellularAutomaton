#Write the output that corresponds to the input state here. Ex: [0,0,1] -> 1
#The current entries are for the Rule 110 Cellular Automaton
class Rules(object):
    object.states = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ]
    object.rules = [
        0,
        1,
        1,
        0,
        1,
        1,
        0,
        1
    ]
