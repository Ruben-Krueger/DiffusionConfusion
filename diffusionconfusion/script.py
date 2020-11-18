from compartments import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import visualization as viz

# kinetic parameters from https://www.sciencedirect.com/science/article/pii/S2090506816300136#b0010
# it must be the case that K_B > K_T > K_E, or else negative concentrations are possible
K_T = 0.3293
K_B = 0.9776
K_E = 0.2213

# K_B = 0.5
# K_E = 0.05
# K_T = 0.25

C_0 = 10


def main():
    diseases = {
        "bp": 1.2,
        "hr": 4,
        "permeability": 0.4
        }

    arterial_blood = ArterialBlood(C_0, K_B, diseases=diseases)
    tissue = Tissue( C_0, K_B, K_T, diseases=diseases)
    venous_blood = VenousBlood(C_0, K_B, K_T, K_E, diseases=diseases)

    # arterial_blood = ArterialBlood(C_0, K_B)
    # tissue = Tissue(C_0, K_B, K_T)
    # venous_blood = VenousBlood(C_0, K_B, K_T, K_E)

    viz.plot_concentration_graph(arterial_blood, tissue, venous_blood, iters=20)
    # visualization.plot_compartment_concentrations(arterial_blood, tissue, venous_blood, iters=20)

    # for l in range(100):
    #     plt.clf()
    #     grid = tissue.grid
    #     plt.pcolor(grid)
    #     plt.colorbar()
    #     plt.xlabel("Iteration %d"%l)
    #     plt.pause(0.1)
    #     tissue.update(1)

if __name__ == "__main__":
    main()


