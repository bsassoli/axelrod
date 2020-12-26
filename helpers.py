import random
import networkx as nx
import matplotlib.pyplot as plt
from axelrod import Lattice


def get_random_color(pastel_factor=0.5):
    return [(x+pastel_factor)/(1.0+pastel_factor) for x in [
        random.uniform(0, 1.0) for i in [1, 2, 3]]]


def color_distance(c1, c2):
    return sum([abs(x[0]-x[1]) for x in zip(c1, c2)])


def generate_new_color(existing_colors, pastel_factor=0.2):
    max_distance = None
    best_color = None
    for i in range(0, 100):
        color = get_random_color(pastel_factor=pastel_factor)
        if not existing_colors:
            return color
        best_distance = min([color_distance(color, c)
                             for c in existing_colors])
        if not max_distance or best_distance > max_distance:
            max_distance = best_distance
            best_color = color
    return best_color


def make_color_snapshot(model):
    initial_cultures = (len(model.get_culture_count()),
                        model.get_culture_count())
    mapping = {}
    for index, culture in enumerate(initial_cultures[1].keys()):
        mapping[culture] = generate_new_color(mapping.values())
    plt.figure()
    for row in range(model.size):
        for col in range(model.size):
            plt.scatter(row, col, s=128, color=tuple(mapping[
                str(model.lattice[row][col])]), marker="H")
    plt.show()


def generate_graph(model):
    G = nx.Graph()
    g = model.lattice
    n = 0
    for row in range(len(g)):
        for col in range(len(g[row])):
            n += 1
            agent = g[row][col]
            G.add_node(n, culture=agent, position=(row, col))
    """
    plt.figure()
    nx.draw(G, with_labels=True)
    plt.show()
    """
    return G


model = Lattice(4, 2, 3)
model.initialize()
g = generate_graph(model)

positions_dic = nx.get_node_attributes(g, 'position')
cultures_dic = nx.get_node_attributes(g, 'culture')
neighbor_dic = {}
for node in g.nodes:
    neighbor_dic[node] = model.get_agent_neighbours(
        positions_dic[node][0], positions_dic[node][1], model.lattice)
print(neighbor_dic)
weights = {}
for agent in g.nodes:
    # map agent to neighbours with attribute weight
    # so a dict with key = agent and values = [neighbour, weight] will do
    # how to get neighbour position??????
    """
    culture = cultures_dic[agent]
    neighbour_cultures = neighbor_dic[agent]
    for neighbour in neighbour_cultures:
    """
