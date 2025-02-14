#Write the output that corresponds to the input state here. Ex: [0,0,1] -> 1
#The current entries are for the Rule 110 Cellular Automaton
from array import array
from Rule import Rule
from RuleSet import RuleSet

class OneDRules(RuleSet):
    def __init__(self, rules):
        super().__init__(rules)
        self.states = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1]
        ]
        self.outputs = [
            0,
            1,
            1,
            0,
            1,
            1,
            0,
            1
        ]
        self.rules = []

    def get_neighbors(self, cell):
        neighbor_array = []



    def output(self, cell, neighbors):
        n = len(self.states)
        neighbor_array = [neighbors[0], cell.alive, neighbors[1]]
        for i in range(1,n):
            if neighbor_array == self.states[i]:
                return self.outputs[i]


