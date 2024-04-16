from math import sqrt

def getDistanceBetweenTwoBodies(pos1, pos2):
    return sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])) * 10e6

def getForceOfAttraction(m1, m2, d):
    GRAVITATIONAL_CONSTANT = 6.6743e-11
    return (GRAVITATIONAL_CONSTANT * m1 * m2)/d**2

def updateVelocity(currentVelocity, mass, force):
    return currentVelocity + (force/mass)