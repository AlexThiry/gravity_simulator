from math import sqrt, cos, sin, atan2

def getDistanceBetweenTwoBodies(pos1, pos2):
    return sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])) * 10e6 #1px = 1 million km

def getForceOfAttraction(m1, m2, d):
    GRAVITATIONAL_CONSTANT = 6.6743e-11
    return (GRAVITATIONAL_CONSTANT * m1 * m2)/d**2

def splitForceVector(f, pos1, pos2):
    deltaY = abs(pos1[1] - pos2[1])
    deltaX = abs(pos1[0] - pos2[0])
    fx = f * cos(atan2(deltaY/deltaX))
    fy = f * sin(atan2(deltaY/deltaX))
    return (fx, fy)

def updateVelocity(currentVelocity, mass, force):
    return [currentVelocity[0] + (force[0]/mass), currentVelocity[1] + (force[1]/mass)]