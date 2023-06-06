import math
import constants

class Body():
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = Vector(position)
        self.velocity = Vector(velocity)
        self.acceleration = Vector((0,0)) 

class Vector():
    def __init__(self, init_tuple):
        self.x = init_tuple[0]
        self.y = init_tuple[1]

    def __add__(self, other):
        if isinstance(other, Vector): return Vector((self.x + other.x, self.y + other.y))
        return Vector((self.x + other, self.y + other))

    def  __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, Vector): return self.x * other.x + self.y * other.y
        return Vector((self.x * other, self.y * other))

    def  __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        return self + other * (-1)

    def  __rsub__(self, other):
        return self.__sub__(other)
    
    def __len__(self):
        return round(math.sqrt(self.x**2 + self.y**2))

def force_between_bodies(b1, b2):
    b1_to_b2 = b2.position - b1.position
    distance = len(b1_to_b2) if len(b1_to_b2) != 0 else 0.5 # this is maybe too inaccurate
    normalized_b1_to_b2 = b1_to_b2 * (1 / distance)
    return normalized_b1_to_b2 * ((constants.GRAVITATIONAL_CONSTANT * b1.mass * b2.mass) / distance**2)
  