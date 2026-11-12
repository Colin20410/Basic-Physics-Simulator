import numpy as np, math; from vectors import Vector; from forces import Force

class ParticleLike:
    def __init__(self, x_pos: float, y_pos: float, z_pos: float, mass: float):
        self.force_list = []
        self.position = Vector("position", x_pos, y_pos, z_pos) #in a future update position vectors may become a separate class with 4th element for time
        self.velocity = Vector("velocity", 0 , 0 , 0)
        self.acceleration = Vector("acceleration", 0 , 0 , 0)
        self.mass = mass

    def boost(self, x: float, y: float, z: float):
        self.velocity[0,0] = x
        self.velocity[0,1] = y
        self.velocity[0,2] = z
