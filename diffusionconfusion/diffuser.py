
from matplotlib.pyplot import *
from matplotlib.animation import FuncAnimation
from numpy import array
from matplotlib import colors
import sys
from vessel import Vessel



class Diffuser:

    def __init__(self, diffusion= 1, seed=None):
        self.vessel = Vessel()
        self.diffusion = diffusion
        self.seed = seed

    def run(self, t, filename=None):
        self.vessel.generate(seed= self.seed)

        ## TODO: Everything else!

        # for i in range(t):
        #     clf()
        #     state = self.vessel.get_state()
        #     pcolor(state)
        #     colorbar()
        #     xlabel("Iteration %d"%l)
        #     pause(0.1)
        #     self.vessel.update()


