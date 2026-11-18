import numpy as np, math; from .vectors import Vector;

class ParticleLike:
    def __init__(self, x_pos: float, y_pos: float, z_pos: float, mass: float):
        from .forces import Force, NetForce
        self.net_force = NetForce( 0 , 0, 0)
        self.force_list = []
        self.position = Vector("position", x_pos, y_pos, z_pos) #in a future update position vectors may become a separate class with 4th element for time
        self.velocity = Vector("velocity", 0 , 0 , 0)
        self.acceleration = Vector("acceleration", 0 , 0 , 0)
        self.mass = mass

    def update_net_force(self):
        from .forces import Force, NetForce
        self.net_force.vector = np.array([[0,0,0,]])
        for i in self.force_list:
            if type(i) == Force:
                self.net_force.vector += i.vector
    
    
    def boost(self, x: float, y: float, z: float):
        self.velocity.vector[0,0] = x
        self.velocity.vector[0,1] = y
        self.velocity.vector[0,2] = z

