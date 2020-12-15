import matplotlib.pyplot as plt
from axelrod import Lattice
from helpers import generate_new_color, generate_graph, make_color_snapshot
import networkx as nx


def run_simulations(no_of_runs, iterations, size_of_grid,
                    no_of_features, no_of_traits):
    plt.figure()
    for _ in range(no_of_runs):
        model = Lattice(size_of_grid, no_of_features, no_of_traits)
        model.initialize()
        iters = iterations
        steps = []
        data = []
        for step in range(iters):
            model.update()
            if (iters - step) % 10000 == 0:
                final_cultures = (len(model.get_culture_count()),
                                  model.get_culture_count())
                steps.append(step)
                data.append(final_cultures[0])
                print(f"Step: {step}. Current cultures: {final_cultures[0]}")
        plt.plot(steps, data)
    plt.show()


# model = Lattice(20, 4, 3)
# model.initialize()
# make_color_snapshot(model)

# graph = generate_graph(model)
# print(nx.get_node_attributes(graph, "culture").values())
# print(graph.nodes[1]["culture"])

run_simulations(5, 1000000, 20, 3, 16)
