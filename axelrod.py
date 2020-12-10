import random
from collections import Counter


class Lattice(object):
    def __init__(self, size, no_features, no_traits):
        self.size = size
        self.no_features = no_features
        self.no_traits = no_traits
        self.lattice = []
        self.total_updates = 0

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
        neighbors = []
        if column not in range(len(lattice)) or row not in range(len(lattice)):
            print("Not in grid")
        # top left
        if column == 0 and row == 0:
            neighbors.append(lattice[row][column+1])
            neighbors.append(lattice[row+1][column])
            neighbors.append(lattice[row+1][column+1])
        # top right
        elif column == size and row == 0:
            neighbors.append(lattice[row][column-1])
            neighbors.append(lattice[row+1][column])
            neighbors.append(lattice[row+1][column-1])
        # bottom left
        elif row == size and column == 0:
            neighbors.append(lattice[row-1][column])
            neighbors.append(lattice[row-1][column + 1])
            neighbors.append(lattice[row][column+1])
        # bottom right:
        elif row == size and column == size:
            neighbors.append(lattice[row-1][column])
            neighbors.append(lattice[row-1][column - 1])
            neighbors.append(lattice[row][column-1])
        # top row
        elif row == 0 and column != 0:
            neighbors.append(lattice[row][column-1])
            neighbors.append(lattice[row][column+1])
            neighbors.append(lattice[row+1][column-1])
            neighbors.append(lattice[row+1][column+1])
            neighbors.append(lattice[row+1][column])
        # bottom row
        elif row == size and column != size:
            neighbors.append(lattice[row][column-1])
            neighbors.append(lattice[row][column+1])
            neighbors.append(lattice[row-1][column-1])
            neighbors.append(lattice[row-1][column+1])
            neighbors.append(lattice[row-1][column])
        # first column
        elif column == 0 and row != 0:
            neighbors.append(lattice[row][column+1])
            neighbors.append(lattice[row-1][column])
            neighbors.append(lattice[row-1][column+1])
            neighbors.append(lattice[row+1][column])
            neighbors.append(lattice[row+1][column+1])
        # last column
        elif column == size and row != size:
            neighbors.append(lattice[row][column-1])
            neighbors.append(lattice[row-1][column])
            neighbors.append(lattice[row-1][column-1])
            neighbors.append(lattice[row+1][column])
            neighbors.append(lattice[row+1][column-1])
        else:
            neighbors.append(lattice[row][column-1])
            neighbors.append(lattice[row][column+1])
            neighbors.append(lattice[row-1][column-1])
            neighbors.append(lattice[row-1][column])
            neighbors.append(lattice[row-1][column+1])
            neighbors.append(lattice[row+1][column-1])
            neighbors.append(lattice[row+1][column])
            neighbors.append(lattice[row+1][column+1])
        return neighbors

    def update(self):

        active_agent_row, active_agent_column = (random.randint(
                        0, self.size-1), random.randint(0, self.size-1))
        active_agent = self.lattice[active_agent_row][active_agent_column]
        neighbours = self.get_agent_neighbours(
                            active_agent_row,
                            active_agent_column, self.lattice)
        neighbour = random.choice(neighbours)
        prob = sum([active_agent[n] == neighbour[n] for n in range(
            self.no_features-1)])/self.no_features
        diff_traits = [neighbour[n] for n in range(
            len(neighbour)) if neighbour[n] != active_agent[n]]
        if random.random() >= prob and diff_traits != []:
            active_agent[random.randint(
                0, self.no_features-1)] = random.choice(diff_traits)
            self.total_updates += 1
        return self.lattice, self.total_updates

    def get_culture_count(self):
        return Counter(str(culture)
                       for row in self.lattice for culture in row)

    def __str__(self):
        ans = "\n"
        for row in self.lattice:
            ans += str(row) + "\n"
        return ans


model = Lattice(5, 2, 4)
model.initialize()
initial_cultures = (len(model.get_culture_count()), model.get_culture_count())
iters = 100000
for _ in range(iters):
    model.update()
    if (iters - _) % 1000 == 0:
        print(iters - _)

print("Mutations: " + str(model.update()[1]))
final_cultures = (len(model.get_culture_count()), model.get_culture_count())
print(initial_cultures)
print(final_cultures)


# Tests for neighbours
# print(model.get_agent_neighbours(0, 0, model.lattice))
# print(model.get_agent_neighbours(2, 2, model.lattice))
# print(model.get_agent_neighbours(0, 2, model.lattice))
# print(model.get_agent_neighbours(2, 0, model.lattice))
# print(model.get_agent_neighbours(0, 1, model.lattice))
# print(model.get_agent_neighbours(2, 1, model.lattice))
# print(model.get_agent_neighbours(1, 0, model.lattice))
# print(model.get_agent_neighbours(1, 2, model.lattice))
# print(model.get_agent_neighbours(1, 1, model.lattice))
