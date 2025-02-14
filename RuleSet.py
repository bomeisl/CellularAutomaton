from array import ArrayType, array
from typing import Protocol

class RuleSet(Protocol):

    def get_neighbors(self, cell, lattice) -> array:
        pass

    def output(self, cell, neighbor_array) -> int:
        pass










