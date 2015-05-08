import math

class Vector3:
    """Vector class in 3 dimensions"""
    
    def __init__(self, x=0 ,y=0, z=0):
        """Create a vector"""
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        """Return the length of the vector"""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def dot(self,vect):
        """Dot product of self and vect"""
        return self.x*vect.x + self.y*vect.y + self.z*vect.z

    def direction(self):
        """Return the unit direction vector"""
        norm=math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return Vector3(self.x/norm, self.y/norm, self.z/norm)

    def cross(self,vect):
        """Cross product"""
        return Vector3(self.y*vect.z - self.z*vect.y, -self.x*vect.z + self.z*vect.x, self.x*vect.y - self.y*vect.x)

    def __add__(self,vect):
        """Vector addition"""
        return Vector3(self.x + vect.x, self.y + vect.y, self.z + vect.z)

    __radd__ = __add__

    def __sub__(self,vect):
        """Vector addition"""
        return Vector3(self.x - vect.x, self.y - vect.y, self.z - vect.z)

    __rsub__ = __sub__

    def __mul__(self,scalar):
        """Vector multiplication"""
        return Vector3(self.x*scalar, self.y*scalar, self.z*scalar)
    
    __rmul__ = __mul__

    def __div__(self,scalar):
        """Overloading / operator"""
        return Vector3(self.x/scalar,self.y/scalar,self.z/scalar)

    def __neg__(self):
        return Vector3(-self.x,-self.y,-self.z)

    def __str__(self):
        """Returns vector's components"""
        return "x = " + str(self.x) + '\ny = ' + str(self.y)+ '\nz = ' + str(self.z)
