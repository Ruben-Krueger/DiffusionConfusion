"""
    The script used in our analysis.
"""

from compartments import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()
import visualization as viz

def main():

    diseases = {
        "bp": 1.2,
        "hr": 4,
        "permeability": 0.4
        }

    bp = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    hr = [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]
    permeability = [0.8, 0.9, 1.0, 1.1, 1.2]
    fluids = [0.8, 0.9, 1.0, 1.1, 1.2]
    # physiology = {"bp": bp, "hr": hr, "permeability": permeability}

    K_T = 0.3293 
    K_B = 0.9776
    K_E = 0.2213
    C_0 = 10

    arterial_blood = ArterialBlood(C_0, K_B, diseases=diseases)
    tissue = Tissue(C_0, K_B, K_T, diseases=diseases)
    venous_blood = VenousBlood(C_0, K_B, K_T, K_E, diseases=diseases)

    # arterial_blood = ArterialBlood(C_0, K_B)
    # tissue = Tissue(C_0, K_B, K_T)
    # venous_blood = VenousBlood(C_0, K_B, K_T, K_E)

    # viz.plot_tissue_diffusion(tissue, 200)

    viz.plot_concentration_graph(arterial_blood, tissue, venous_blood, iters=20)
    # visualization.plot_compartment_concentrations(arterial_blood, tissue, venous_blood, iters=20)

    # viz.analyze_convergence("bp", bp, C_0, K_B, K_T)

if __name__ == "__main__":
    main()


