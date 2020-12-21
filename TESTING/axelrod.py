import random
from collections import Counter


class Lattice(object):
    """A class representing a model.
    A n x n 2d-array where every item represents an agent - or culture.
    An agent is a represented by a list of traits, one for each feature.

    Attributes:
        size (int) : the size of a size x size array
        no_features (int) : the lenght of every item in the array
        no_traits (int) : the possible values that every feature can take
        lattice (list): the list representation of the model.
        total_updates (int): the overall mutations the model's agent underwent
    """
    def __init__(self, size, no_features, no_traits):
        """Creates an instance of a lattice
        Arguments:
            size (int): the size of a square 2-d array
            no_features (int): the number of features for each agent
            no_traits (int): the possible values a feature can take

        """
        self.size = size
        self.no_features = no_features
        self.no_traits = no_traits
        self.lattice = []
        self.total_updates = 0

    def initialize(self):
        """Initializes a NxN Lattice populating each cell with an agent.

        Returns:
            A list of lists.
        """
        for a in range(self.size):
            row = []
            for column in range(self.size):
                agent = [random.randint(0, self.no_traits)
                         for _ in range(self.no_features)]
                row.append(agent)
            self.lattice.append(row)
        return self.lattice

    def get_agent_neighbours(self, row, column, lattice):
        """
        Arguments:
            row (int): the agent's X position in a lattice
            column (int): the agent's Y position in a lattice
            lattice: the 2x2 array to be searched

        Returns:
            a list of all the adjacent agents for the given position
        """
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
        """
        Runs a single update of the lattice.

        """
        mutations = []
        active_agent_row, active_agent_column = (random.randint(
                        0, self.size-1), random.randint(0, self.size-1))
        active_agent = self.lattice[active_agent_row][active_agent_column]
        neighbours = self.get_agent_neighbours(
                            active_agent_row,
                            active_agent_column, self.lattice)
        neighbour = random.choice(neighbours)
        diff_vector = [neighbour[n] != active_agent[n] for n in range(len(
            neighbour))]
        diff_traits = [index for index in range(
            len(diff_vector)) if diff_vector[index] == 1]
        prob = (self.no_features-len(diff_traits))/self.no_features
        # print(f"Active: {active_agent}, neighbour; {neighbour}, prob: {
        # prob}, diff_vector {diff_vector}, diff_traits: {diff_traits}")
        if random.random() <= prob and diff_traits != []:
            # print("Mutating")
            index = random.choice(diff_traits)
            active_agent[index] = neighbour[index]
            mutations.append([(active_agent_row, active_agent_column),
                             active_agent])
            self.total_updates += 1
        return self.lattice, mutations, self.total_updates

    def get_list(self):
        return list(self.lattice)

    def get_culture_count(self):
        return Counter(str(culture)
                       for row in self.lattice for culture in row)

    def get_cumulative_mutations(self):
        return self.total_updates

    def equilibrium(self):
        for row in range(self.size):
            for column in range(self.size):
                neighbours = self.get_agent_neighbours(
                             row, column, self.lattice)
                active_agent = self.lattice[row][column]
                for neighbour in neighbours:
                    # does every neighbour of the agent's differ
                    # in one or more but not all traits?
                    # If at least one agent doesn't:
                    # --> no equilibrium, return False
                    # Else: keep checking
                    diff_vector = sum([neighbour[n] != active_agent[
                                  n] for n in range(len(neighbour))])
                    if diff_vector != 0 and diff_vector != self.no_features:
                        return False
        return True

    def __str__(self):
        ans = "\n"
        for row in self.lattice:
            ans += str(row) + "\n"
        return ans


"""
iters = 5000000
for step in range(iters):
    model.update()
    if (iters - step) % 10000 == 0:
        final_cultures = (len(model.get_culture_count()),
                          model.get_culture_count())
        print(f"Step: {step}. Current cultures: {final_cultures[0]}")

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
"""
