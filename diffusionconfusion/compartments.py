"""
    An extended version of the three compartment model described by Khanday et al.
"""


import numpy as np
from math import ceil
import random


class Tissue:
    """
        Models the tissue compartment in the three-compartment model. Note: nextX(), nextY(), and diffusion() are largely derived from
        Assignment 2.
    """

    def __init__(self, c_0, k_b, k_t, nX=10, nY=10, diseases=None, t=0, epsilon=1e-2, D=1):
        self.nX = nX
        self.nY = nY
        self.c_0 = c_0
        self.c = c_0
        self.t = t    
        self.k_b = k_b
        self.k_t = k_t    
        self.blocks = np.zeros((nX, nY))
        self.blocks[0] = c_0
        self.diseases = diseases
        self.D = D
        self.epsilon = epsilon
        self.converged = False
    
    @property
    def grid(self):
        return self.blocks

    def update(self, delta_t=1):
        self.t += delta_t
        a = (self.c_0 * self.k_b) / (self.k_b - self.k_t)
        if self.diseases:
            # b = np.exp(-self.k_t * self.t) - np.exp(-self.k_b * self.t) * np.log(self.c_0 * self.diseases["hr"] *  self.diseases["bp"] + 1)
            b = np.exp(-self.k_t * self.t) - np.exp(-self.k_b * self.t) + np.log(self.c_0 * self.diseases["hr"] * self.diseases["bp"])
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
                particles = ceil(self.blocks[row][col])
                delta = ceil(self.D)

                for particle in range(particles):
                    stepSize = delta - (random.random() > 0.7)
    
                    direction = random.choice(["left", "right", "up", "down"])
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
        self.blocks = self.blocks * (self.c / self.blocks.sum()) if np.mean(self.blocks) > self.epsilon else np.zeros((self.nY, self.nX))
        if np.mean(self.blocks) < self.epsilon and not self.converged:
            self.converged = self.t

class ArterialBlood:
    """
        Models the arterial blood compartment in the three-compartment model. 
    """
    def __init__(self, c_0, k_b, diseases=None, t=0):
        self.c_0 = c_0
        self.c = c_0 
        self.t = t
        self.k_b = k_b        
        self.diseases = diseases

    def update(self, delta_t=1):
        self.t += delta_t
        if self.diseases:
            self.c = np.log(self.c * self.diseases["hr"] * self.diseases["bp"]) * self.c_0 + self.diseases["permeability"] * self.c_0 * np.exp(-self.k_b * self.t) - self.t * np.exp(-self.k_b)
            # self.c = np.log(self.c * self.diseases["hr"] *  self.diseases["bp"] + 1) * self.c_0 * np.exp(-self.k_b * self.t)
        else:
            self.c = self.c_0 * np.exp(-self.k_b * self.t)


class VenousBlood:
    """
        Models the venous blood compartment in the three-compartment model. 
    """


    def __init__(self, c_0, k_b, k_t, k_e, diseases=None, t = 0):
        self.c_0 = c_0
        self.c = c_0 
        self.t = t
        self.k_b = k_b        
        self.k_t = k_t
        self.k_e = k_e
        self.diseases = diseases

    def update(self, delta_t=1):
        self.t += delta_t
        a  = np.exp(- self.k_t * self.t) / ((self.k_b - self.k_t) * (self.k_e - self.k_t)) 
        b = np.exp(- self.k_b * self.t) / ((self.k_b - self.k_t) * (self.k_e - self.k_b)) 
        c = np.exp(-self.k_e * self.t) / ((self.k_e - self.k_t) * (self.k_e - self.k_b))
        if self.diseases:   
            # self.c = np.log(self.c_0 * self.diseases["hr"] *  self.diseases["bp"] + 1) * self.c_0 * self.k_t * self.k_b * (a - b + c)
            self.c = np.log(self.c_0 * self.diseases["hr"] * self.diseases["bp"]) + self.diseases["permeability"] * self.c_0 * self.k_t * self.k_b * (a - b + c)
        else:        
            self.c = self.c_0 * self.k_t * self.k_b * (a - b + c)
