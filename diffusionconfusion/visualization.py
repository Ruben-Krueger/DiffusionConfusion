from compartments import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import seaborn as sns
import random
from itertools import count
import pandas as pd
from matplotlib import colors

# plt.style.use('fivethirtyeight')

# x_vals = []
# y_vals = []

# index = count()


# def animate(i):
#     data = pd.read_csv('data.csv')
#     x = data['x_value']
#     y1 = data['total_1']
#     y2 = data['total_2']

#     plt.cla()

#     plt.plot(x, y1, label='Channel 1')
#     plt.plot(x, y2, label='Channel 2')

#     plt.legend(loc='upper left')
#     plt.tight_layout()


# ani = FuncAnimation(plt.gcf(), animate, interval=1000)

# plt.tight_layout()
# plt.show()

#  plt.arrow(x_pos, y_pos, x_scale * length, y_scale * length,
#                   fc=fc, ec=ec, alpha=alpha, width=width,
#                   head_width=head_width, head_length=head_length,
#                   **arrow_params)


def plot_compartment_concentrations(arterial_blood, tissue, venous_blood, interval=0.5, iters=100, console_out=False):

    # ani = FuncAnimation(plt.gcf(), animate, interval=1000)
    # plt.legend()
    # plt.show()

    # fig, axs = plt.subplots(2)
    # fig.suptitle('Vertically stacked subplots')
    # axs[0].plot(x, y)
    # axs[1].plot(x, -y)

    for l in range(iters):
        plt.clf()
        tg = tissue.grid
        plt.pcolormesh(tg)

        # ax=plt.gca() #get the current axes
        # PCM=ax.get_children()[2] #get the mappable, the 1st and the 2nd are the x and y axes
        # plt.colorbar(PCM, ax=ax) 

        plt.colorbar()
        plt.xlabel("Iteration %d"%l)
        plt.pause(interval)
        animate(arterial_blood, tissue, venous_blood, l, console_out)


#  for l in range(iters):
#     clf()
#     grid = c.getGrid()
#     pcolor(array([i for i in xrange(length+1)]),array([j for j in xrange(length+1)]),grid,cmap = cm)
#     colorbar()
#     #un-comment the line below to 'fix' the colorbar to the range [0,3] so it is not longer dynamic
#     #clim(0,3) 
#     xlabel("Iteration %d"%l)
#     pause(0.1)
#     c.simulateTimeStep(1)

    # for i in range(iters):
    #     animate(arterial_blood, tissue, venous_blood, console_out)
    #     a += [arterial_blood.c]
    #     t += [tissue.c]
    #     v += [venous_blood.c]


def plot_tissue_diffusion(tissue, iters=100):
    c = []
    for i in range(iters):
        tissue.update(1)
        c += [tissue.c]
    


def animate(arterial_blood, tissue, venous_blood, iteration, console_out=False):
    arterial_blood.update(1)
    tissue.update(1)
    venous_blood.update(1)

    if console_out:
        print(f"t={iteration}")
        print(f"Arterial blood c: {arterial_blood.c}")
        print(f"Tissue c: {tissue.c}")
        print(f"Venous blood c: {venous_blood.c}")

def plot_concentration_graph(arterial_blood, tissue, venous_blood, iters=100, console_out=False):

    a, t, v = [], [], []

    for i in range(iters):
        animate(arterial_blood, tissue, venous_blood, console_out)
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