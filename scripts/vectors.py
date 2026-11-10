import numpy as np, math

class Vector: 
    def __init__(self, type: str,  x: float, y: float, z: float): 
        self.type = type #Type to categorize vectors by physical quantities in physics scripts
        self.magnitude = round(math.sqrt((x*x + y*y + z*z)) , 3)
        self.vector = np.array([[x,y,z]])


    def __repr__(self):
        return f"Vector <{self.vector[0,0]} , {self.vector[0,1]}, {self.vector[0,2]}> of type: {self.type}"

    def __eq__(self, altVec):
        if not isinstance(altVec, type(self)):
            return False

        if not self.type == altVec.type:
            return False
        if not np.array_equal(self.vector, altVec.vector):
            return False
        else:
            return True

    def __neg__(self):
        neg = type(self)(self.type, -self.vector[0,0], -self.vector[0,1], -self.vector[0,2]) #type() is used here to account for future subclasses that will be added
        return neg

    def __add__(self, altVec) -> Vector:
        
        if self.type == altVec.type:
            add = Vector(self.type, 0, 0, 0)
            for i in range(0,3):
               add.vector[0,i] = self.vector[0,i] + altVec.vector[0,i]
            add.updateMag()
            return add

        else:
           print("Couldn't subtract; Incompatible Vector objects")
           return None

    def __sub__(self, altVec) -> Vector:
        
        if self.type == altVec.type:
            sub = Vector(self.type, 0, 0, 0)
            for i in range(0,3):
               sub.vector[0,i] = self.vector[0,i] - altVec.vector[0,i]
            sub.updateMag()
            return sub

        else:
           print("Couldn't subtract; Incompatible Vector objects")
           return None

    def __mul__(self, altVec) -> Vector:
        #Matrix Set up

        tool = np.empty((2,3))


        tool[0,:] = self.vector
        tool[1,:] = altVec.vector

        #Apply Cofactor Expansion

        i_mat = tool[0:, 1:]
        j_mat = tool[0:,0::2]
        k_mat = tool[0:,:2]

        i = np.linalg.det(i_mat)
        j = -1 * np.linalg.det(j_mat)
        k = np.linalg.det(k_mat)

        cross = Vector(self.type, i, j, k)
        return cross

    def dot(self, altVec) -> float:
       dot = 0
       for i in range(0,3):
          dot += self.vector[0, i] * altVec.vector[0, i]
       return dot

    def update_mag(self):
        mag = 0
        for i in range(0,3):
            mag += math.pow(self.vector[0,i], 2)
        mag = round(math.sqrt(mag), 3)
        self.magnitude = mag


       