import pylab
import math
import Vector3
import Particle
import Force
    
def Euler(particle,force,dt):
    """Return particle with updated acc, vel, pos"""
    particle.acc = force/particle.m
    particle.vel = particle.vel + particle.acc*dt
    particle.pos = particle.pos + particle.vel*dt
    
    return particle

#------------------------------------MAIN------------------------------------#
#This main code is to calculate the distance separation between two particles

def bounce(par, par2, freq):
    """Return the value of position z, position z2, time, and separation between two particles"""

    F1=Force(par) #Make Force class

    #Define empty matrices
    z=[] 
    z2=[]
    t=[]
    sepo = 0.0 #Initial condition for separation
    
    for i in xrange(0,500000):
        t.append(i*0.0001) #add element i*0.0001 to matrix t
        par2.pos.z = -500 + 10*math.sin(freq*t[i]) #The oscillating part from the plate
        netF = F1.GravitationalF(9.8) + F1.NormalF(par2,1000000,1,0.00001) + F1.FrictionF(0.2) #Net force calculation
        par = Euler(par,netF,0.0001) #Updating particle 1
        par2 = Euler(par2,Vector3(0,0,0),0.0001) #Updating particle 2
        z.append(par.pos.z-0.5) #add z position of particle 1 to matrix z
        z2.append(par2.pos.z+500) #add z position of particle 2 to matrix z2

        #Calculating the separation between two particles after stable time
        if t[i] > (0.0001*200000-2*3.14/freq):
            sepn = (par.pos.z-0.5) - (par2.pos.z+500)
            if sepn > sepo:
                sepo = sepn

    return z,z2,t,sepo

f = open("massa1.1.txt","w") #Open file .txt to be written
n=1

freq = [0.15+i*0.01 for i in xrange(0,n)] #The matrix for omega (note we want to take range of omega values)

#Creating zero and empty matrices
z=[[0 for j in xrange(0,200000)] for k in xrange(0,n)]
z2=[[0 for j in xrange(0,200000)] for k in xrange(0,n)]
t=[[0 for j in xrange(0,200000)] for k in xrange(0,n)]
sep=[]

#Iteration for range of omega
for i in xrange(0,n):
    #Initializaition of particle 1 and the particle for plate
    pos = Vector3(0.0,0.0,0.5)
    vel = Vector3(0.0,0.0,0.0)
    acc = Vector3(0,0,0)
    par = Particle(pos,vel,acc,1,1)

    pos2=Vector3(0.0,0.0,-500.0)
    vel2=Vector3(0.0,0.0,0.0)
    zero=Vector3(0,0,0)
    par2=Particle(pos2,vel2,zero,1,1000)

    z[i],z2[i],t[i],sepo=bounce(par,par2,freq[i])
    f.write(str(sepo) + "\t" + str(freq[i]) + "\n") #Write to file
    sep.append(sepo) #add sepo to matrix sep
    print sepo

f.close() #Close the file

#These lines are for drawing the figure using pylab
pylab.figure(1)
pylab.xlabel('t')
pylab.ylabel('z')
pylab.plot(t[0],z[0])
pylab.plot(t[0],z2[0])
pylab.show()
