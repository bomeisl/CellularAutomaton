import random
from Cell import Cell


class Lattice:
    def __init__(self,n,m):
        self.lattice = []
        for i in range(n-1):
            row = []
            for j in range(m-1):
                seed = random.randint(0,1)
                row.append(seed)
            self.lattice.append(row)
        self.neighbors = [
            [1,0],
            [0,1],
            [-1,0],
            [0,-1],
            [1,1],
            [-1,-1],
            [-1,1],
            [1,-1]
        ]

    def evolve(self):
        for i in range(self.n-1):
            for j in range(self.m-1):
                cell = Cell(i,j)
                neighbor_array = []
                for neighbor in self.neighbors:
                    cell = Cell(i+neighbor[0],j+neighbor[1])
                    neighbor_array.append(cell.alive)
                new_cell = cell.evolve(neighbor_array)
                self.lattice[i][j] = new_cell



