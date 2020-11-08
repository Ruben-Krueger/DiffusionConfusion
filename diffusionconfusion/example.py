from compartments import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# kinetic parameters from https://www.sciencedirect.com/science/article/pii/S2090506816300136#b0010
K_T = 0.3293
K_B = 0.9776
K_E = 0.2213
C_0 = 500

ITERS = 10



def main():
    arterial_blood = ArterialBlood(C_0, K_B)
    tissue = Tissue(100, 100, C_0, K_B, K_T)
    venous_blood = VenousBlood(C_0, K_B, K_T, K_E)

    a, t, v = [], [], []

    for _ in range(ITERS):
        arterial_blood.update(1)
        tissue.update(1)
        venous_blood.update(1)
        print(f"t={t}")
        print(f"Arterial blood c: {arterial_blood.c}")
        print(f"Tissue c: {tissue.c}")
        print(f"Venous blood c: {venous_blood.c}")

        a += [arterial_blood.c]
        t += [tissue.c]
        v += [venous_blood.c]

    sns.set_style("darkgrid")
    fig, ax = plt.subplots()
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    ax.plot(a, label="arterial blood")
    ax.plot(t, label="tissue")
    ax.plot(v, label="venous blood")
    leg = ax.legend()
    plt.show()


if __name__ == "__main__":
    main()