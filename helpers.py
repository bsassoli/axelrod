import random
import networkx as nx
import matplotlib.pyplot as plt


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
            G.add_node(n, culture=agent)
    """
    weights = [node for node in G.nodes]
    print(weights)
    plt.figure()
    nx.draw(G, with_labels=True)
    plt.show()
    """
    return G
