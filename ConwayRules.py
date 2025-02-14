from array import array

from RuleSet import RuleSet

class ConwayRules(RuleSet):
    def __init__(self):
        self.neighbor_coord = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
            [1, 1],
            [-1, -1],
            [-1, 1],
            [1, -1]
        ]

    def get_neighbors(self, cell, lattice) -> array:
        neighbor_array = []
        for coord in self.neighbor_coord:
            x = cell.x
            y = cell.y
            neighbor = lattice.lattice[x + coord[0], y + coord[1]]
            neighbor_array.append(neighbor)

    def output(self, cell, neighbor_array) -> int:
        #apply the logic of the automaton to get the new cell value
        pass








