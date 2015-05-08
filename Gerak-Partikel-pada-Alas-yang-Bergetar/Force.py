import Vector3
import Particle

def diff(fx,fxdx,dx):
    """Function to differentiate"""
    result = (fxdx - fx) / dx
    return result

def EulerN(particle,dt):
    """To be used in NormalF calculation only"""
    particle.acc = particle.acc
    particle.vel = particle.vel + particle.acc*dt
    particle.pos = particle.pos + particle.vel*dt

    return particle

class Force(particle.Particle):
    """Class Force"""

    def __init__(self,particle):
        """Creating force calculator in a particle"""
        self.par = particle
    
    def GravitationalF(self,g):
        """Calculating gravitational force"""
        return -self.par.m*Vector3(0,0,g)

    def FrictionF(self,eta):
        """Calculating frictional force due to air"""
        return -3*3.14*eta*self.par.d*self.par.vel

    def NormalF(self,other, kn, gamman, dt):
        """Calculating normal force due to collision between two particles"""
        return (kn*self.par.overlap(other)+gamman*diff(self.par.overlap(other),EulerN(self.par,dt).overlap(other),dt))*(self.par.pos-other.pos).direction()
