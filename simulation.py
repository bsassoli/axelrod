import matplotlib.pyplot as plt
from axelrod import Lattice


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
                if model.equilibrium() is True:
                    print("Equilibrium")
                    break
                else:
                    print(
                        f"Step: {step}. Current cultures: {final_cultures[0]}")
        plt.plot(steps, data)
    plt.show()


# run_simulations(3, 4000000, 40, 3, 4)

"""
for _ in range(100):
    model.update()
    make_color_snapshot(model)
"""
