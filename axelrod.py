import random


class Lattice(object):
    def __init__(self, size, no_features, no_traits):
        self.size = size
        self.no_features = no_features
        self.no_traits = no_traits
        self.lattice = []

    def initialize(self):
        """
        Initializes a NxN lattice populating each cell with an agent.
        """
        for row in range(self.size):
            row = []
            for column in range(self.size):
                agent = [random.randint(1, self.no_traits)
                         for _ in range(self.no_features)]
                row.append(agent)
            self.lattice.append(row)
        return self.lattice

    def get_agent_neighbours(self, row, column, lattice):
        size = len(lattice)-1
        new_lattice = lattice.copy()
        if column == size:
            new_lattice = [[pos[column-1], pos[column], pos[0]]
                           for pos in lattice]
        elif column == 0:
            new_lattice = [[pos[size], pos[column], pos[column+1]]
                           for pos in lattice]
        row_lattice = new_lattice.copy()
        if row == size:
            row_lattice = [new_lattice[row-1],
                           new_lattice[row],
                           new_lattice[0]]
        elif row == 0:
            row_lattice = [new_lattice[size],
                           new_lattice[row],
                           new_lattice[row+1]]
        row_lattice[1].pop(1)
        return [item for row in row_lattice for item in row]

    def update(self):
        active_agent = (random.randint(
                        0, self.size-1), random.randint(0, self.size-1))
        neighbours = self.get_agent_neighbours(
                            active_agent[0],
                            active_agent[1], self.lattice)
        probs = [sum([item == trait for item in active_agent
                     for trait in neighbour])/self.no_features
                 for neighbour in neighbours]
        for prob in range(len(probs)):
            print(neighbours[prob])
            if random.random() >= probs[prob]:
                self.lattice[active_agent[0]][active_agent[1]][
                    random.randint(0, self.no_features-1)] = neighbours[prob][
                        random.randint(0, self.no_features-1)]

    def __str__(self):
        ans = "\n"
        for row in self.lattice:
            ans += str(row) + "\n"
        return ans


model = Lattice(3, 4, 10)
print(model.initialize())
print(model)
for _ in range(40):
    print("Update " + str(_))
    model.update()
print(model)
exit
