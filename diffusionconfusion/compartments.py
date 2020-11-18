# Four major factors interact to affect blood pressure: 
# cardiac output, blood volume, peripheral resistance, and viscosity
import numpy as np
from math import ceil

class Tissue():

    def __init__(self, c_0, k_b, k_t, nX = 10, nY = 10, diseases=None, t = 0):
        self.nX = nX
        self.nY = nY
        self.c_0 = c_0
        self.c = c_0
        self.t = t    
        self.k_b = k_b
        self.k_t = k_t    
        self.blocks = np.full((nX, nY), c_0 / (nX * nY))
        self.diseases = diseases
        self.D = 20
    
    @property
    def grid(self):
        return self.blocks

    def update(self, delta_t):
        self.t += delta_t
        a = (self.c_0 * self.k_b) / (self.k_b - self.k_t)
        if self.diseases:
            b = np.exp(-self.k_t * self.t) - np.exp(-self.k_b * self.t) * np.log(self.c_0 * self.diseases["hr"] *  self.diseases["bp"] + 1)
        else: 
            b = np.exp(-self.k_t * self.t) - np.exp(-self.k_b * self.t)   

        self.c = a * b
        self.diffusion()

    def nextX(self, x, step):
        return int((x+step)%self.nX)

    def nextY(self,y,step):
        return int((y+step)%self.nY)

    def diffusion(self):
        # First, all values in new blocks are set to 0
        newBlocks = np.zeros((self.nY, self.nX))

        for row in range(self.nY): 
            for col in range(self.nX):
                particles = self.blocks[row][col]
                delta = ceil(self.D)

                # Now we will iterate through every particle in each block
                for part in range(int(particles)): 
                    stepSize = delta - (random() > 0.7)
                    
                    direction = choice(["left", "right", "up", "down"])
                    if direction == "left":
                        d = self.nextX(row, -stepSize)
                        newBlocks[d][col] += 1
                    elif direction == "right":
                        d = self.nextX(row, stepSize)
                        newBlocks[d][col] += 1
                    elif direction == "up":
                        d = self.nextY(col, -stepSize)
                        newBlocks[row][d] += 1
                    else:
                        d = self.nextY(col, stepSize)
                        newBlocks[row][d] += 1

        self.blocks = newBlocks


class ArterialBlood():

    def __init__(self, c_0, k_b, diseases=None, t = 0):
        self.c_0 = c_0
        self.c = c_0 
        self.t = t
        self.k_b = k_b        
        self.diseases = diseases

    def update(self, delta_t):
        self.t += delta_t
        if self.diseases:
            self.c = np.log(self.c * self.diseases["hr"] *  self.diseases["bp"] + 1) * self.c_0 * np.exp(-self.k_b * self.t)
        else:
            self.c = self.c_0 * np.exp(-self.k_b * self.t)


class VenousBlood():

    def __init__(self, c_0, k_b, k_t, k_e, diseases=None, t = 0):
        self.c_0 = c_0
        self.c = c_0 
        self.t = t
        self.k_b = k_b        
        self.k_t = k_t
        self.k_e = k_e
        self.diseases = diseases

    def update(self, delta_t):
        self.t += delta_t
        a  = np.exp(- self.k_t * self.t) / ((self.k_b - self.k_t) * (self.k_e - self.k_t)) 
        b = np.exp(- self.k_b * self.t) / ((self.k_b - self.k_t) * (self.k_e - self.k_b)) 
        c = np.exp(-self.k_e * self.t) / ((self.k_e - self.k_t) * (self.k_e - self.k_b))
        if self.diseases:   
            
            # self.c = self.c_0 * self.k_t * self.k_b * (a - b + c) - np.exp (self.c_0 * self.diseases["hr"])    
            #          
            self.c = np.log(self.c_0 * self.diseases["hr"] *  self.diseases["bp"] + 1) * self.c_0 * self.k_t * self.k_b * (a - b + c)
      
        else:        
            self.c = self.c_0 * self.k_t * self.k_b * (a - b + c)
