
# Four major factors interact to affect blood pressure: 
# cardiac output, blood volume, peripheral resistance, and viscosity
import numpy as np

class Compartment(object):

    def __init__(self, c, t = 0):
        self.c = c
        self.t = t       

    def update(self, delta_t, delta_c):
        self.t += delta_c
        self.c += delta_c


class Tissue(Compartment):

    def __init__(self, nX, nY, c_0, k_b, k_t, t = 0):
        self.nX = nX
        self.nY = nY
        self.c_0 = c_0
        self.c = c_0
        self.t = t    
        self.k_b = k_b
        self.k_t = k_t    
        self.blocks = np.zeros((nX, nY))
    

    # a = a * (s/ a.sum()) where s is the desired sum


    def update(self, delta_t):
        self.t += delta_t
        self.c = (self.c_0 * self.k_b / (self.k_b - self.k_t)) * (np.exp(-self.k_t * self.t) - np.exp(-self.k_b * self.t) )


class ArterialBlood(Compartment):

    def __init__(self, c_0, k_b, t = 0):
        self.c_0 = c_0
        self.c = c_0 # current concentration = initial concentration
        self.t = t
        self.k_b = k_b        

    def update(self, delta_t):
        self.t += delta_t
        self.c = self.c_0 * np.exp(-self.k_b * self.t)

class VenousBlood(Compartment):


    def __init__(self, c_0, k_b, k_t, k_e, t = 0):
        self.c_0 = c_0
        self.c = c_0 # current concentration = initial concentration
        self.t = t
        self.k_b = k_b        
        self.k_t = k_t
        self.k_e = k_e

    def update(self, delta_t):
        self.t += delta_t
        
        a  = np.exp(- self.k_t * self.t) / ((self.k_b - self.k_t) * (self.k_e - self.k_t)) 
        b = np.exp(- self.k_b * self.t) / ((self.k_b - self.k_t) * (self.k_e - self.k_b)) 
        c = np.exp(-self.k_e * self.t) / ((self.k_e - self.k_t) * (self.k_e - self.k_b))
        self.c = self.c_0 * self.k_t * self.k_b * (a - b + c)
