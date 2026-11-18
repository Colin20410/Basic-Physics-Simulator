import numpy as np, math 
from .vectors import Vector; from .particle_like import ParticleLike


class Force(Vector):

    def __init__(self, object: ParticleLike , x: float, y: float, z: float):
        super().__init__("Force", x, y, z)
        self.object = object
        self.object.force_list.append(self)
        self.object.update_net_force()

class NetForce(Vector):

    def __init__(self, x: float, y: float, z: float):
        super().__init__("Net Force" , x , y , z)

    def second_law(self, mass): 
        temp_vec = self * (1 / mass)
        return Vector("acceleration", temp_vec.vector[0,0], temp_vec.vector[0,1], temp_vec.vector[0,2])
