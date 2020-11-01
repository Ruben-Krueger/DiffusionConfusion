"""
    Models a blood vessel.

    For Sharon :)
"""

class Vessel:

    def __init__(self) -> None:
        self.blocks = None
        self.target_cells = [] # locations of the target cells

    def generate(self, n_particles: int, seed=None) -> None:
        """  Creates a new blood vessel, with n_particles of drug. """
        raise NotImplementedError("TODO")

    def update(self) -> None:
        """ Performs diffusion and moves blood in vessel. """
        raise NotImplementedError("TODO")

    def evaluate(self, epsilon: int) -> float:
        """ Returns the percentage of particles that reached within epsilon of the target cells. """
        raise NotImplementedError("TODO")

    
    def get_state(self):
        return self.blocks

    