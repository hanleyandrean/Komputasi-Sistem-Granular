import Vector3

class Particle(vector.Vector3):
    """Particle class"""

    def __init__(self, position, velocity, acceleration, mass, diameter):
        """Create a particle"""
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.m = mass
        self.d = diameter

    def overlap(self,other):
        """return the overlap distance between two spherical particles"""
        return max(0,(self.d/2.0+other.d/2.0)-(self.pos-other.pos).length())

    def __str__(self):
        """Returns particle definition"""
        return "mass = " + str(self.m) + "\ndiameter = " + str(self.d) + "\nposition \n" + str(self.pos) + "\nvelocity \n" + str(self.vel) + "\nacceleration \n" + str(self.acc)
