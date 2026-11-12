import numpy as np, math
from vectors import Vector

class Force(Vector):

    def __init__(self, object: str, x: float, y: float, z: float):
        super().__init__("Force", x, y, z)
        self.object = object #Eventually object will be replaced with an object from a particleLike class