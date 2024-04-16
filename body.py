import pygame
from math import sqrt, cos, sin, atan2

class Body():
    def __init__(self, mass, position, velocity, radius, color) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color
        
        self.center = False
    def getForceOfGravity(self, body):
        GRAVITATIONAL_CONSTANT = 6.6743e-11

        pos1 = self.position
        pos2 = body.position
        deltaY = pos1[1] - pos2[1]
        deltaX = pos1[0] - pos2[0]

        d = sqrt(deltaX**2 + deltaY**2) * 10e6 #1px = 1 million km

        f = (GRAVITATIONAL_CONSTANT * set.mass * body.mass)/d**2
        fx = f * cos(atan2(deltaY/deltaX))
        fy = f * sin(atan2(deltaY/deltaX))
        return (fx, fy)
    def updatePos(self, bodies):
        total_fx, total_fy = 0
        for body in bodies:
            if body != self:
                currentForce = self.getForceOfGravity(body)
                total_fx, total_fy += currentForce[0], currentForce[1]
    def draw(self, d):
        pygame.draw.circle(d, self.color, tuple(self.position), self.radius)