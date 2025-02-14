from EvolutionRule import EvolutionRule


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = 0
        self.rules =

    def evolve(self, neighbor_array):
        for rule in self.rules:
            if rule.input_array == neighbor_array:
                return rule.output
