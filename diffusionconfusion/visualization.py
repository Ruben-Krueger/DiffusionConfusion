"""
    Functions for visualizing the three-compartment model.
"""

from compartments import *
import matplotlib.pyplot as plt
import seaborn as sns


def plot_tissue_diffusion(tissue, iters=100):
    for i in range(iters):
        plt.clf()
        grid = tissue.grid
        plt.pcolor(grid)
        plt.colorbar()
        plt.xlabel(f"Iteration {i}")
        plt.pause(0.1)
        tissue.update(1)

def plot_convergence(name, params, C_0, K_B, K_T, iters=1000):
    results = {}
    
    for param in params:
        physiology = {"bp": 1, "hr": 1, "permeability": 1}
        physiology[name] = param
        tissue = Tissue(C_0, K_B, K_T)

        for i in range(iters):
            tissue.update()
            if tissue.converged:
                results[param] = i
                break  

    plt.scatter(range(len(results)), list(results.values()))
    plt.xticks(range(len(results)), list(results.keys()))
    plt.show()

def plot_concentration_graph(arterial_blood, tissue, venous_blood, iters=100, console_out=False):

    a, t, v = [], [], []

    for i in range(iters):
        arterial_blood.update()
        tissue.update()
        venous_blood.update()
        a += [arterial_blood.c]
        t += [tissue.c]
        v += [venous_blood.c]

    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.title("Drug concentrations over time")
    ax.plot(a, label="arterial blood")
    ax.plot(t, label="tissue")
    ax.plot(v, label="venous blood")
    leg = ax.legend()
    plt.show()