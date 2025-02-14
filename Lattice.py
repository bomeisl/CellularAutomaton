from Cell import Cell
from ConwayRules import ConwayRules

class Lattice:
    def __init__(self,n,m,rule_set):
        self.n = n
        self.m = m
        self.lattice = []
        self.rule_set = ConwayRules()
        for i in range(1,n):
            row = []
            for j in range(1,m):
                row.append(Cell(i,j))
            self.lattice.append(row)

    def initial_populate(self):
        for i in range(1,self.n):
            row = []
            for j in range(1,self.m):
                cell = Cell(i,j)
                row.append(cell.alive)
            self.lattice.append(row)

    def evolve(self, rule_set):
        for i in range(1,self.n):
            for j in range(1,self.m):
                cell = Cell(i,j)
                neighbor_array = self.rule_set.get_neighbors(cell, self)
                output = self.rule_set.output(cell, neighbor_array)
                self.lattice[i][j] = output



