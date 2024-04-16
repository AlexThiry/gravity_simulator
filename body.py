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
        deltaX = pos2[0] - pos1[0]
        deltaY = pos2[1] - pos1[1]

        d = sqrt(deltaX**2 + deltaY**2)

        f = (GRAVITATIONAL_CONSTANT * self.mass * body.mass)/d**2
        fx = f * cos(atan2(deltaY, deltaX))
        fy = f * sin(atan2(deltaY, deltaX))
        return (fx, fy)
    
    def updatePos(self, bodies, dt):
        total_fx, total_fy = 0, 0
        for body in bodies:
            if self != body:
                currentForce = self.getForceOfGravity(body)
                total_fx += currentForce[0]
                total_fy += currentForce[1]
        
        self.velocity[0] += total_fx/self.mass * dt
        self.velocity[1] += total_fy/self.mass * dt
        
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
    
    def draw(self, window):
        SCALE = 400/208e9 # 1/10e8 #1px = 1,000,000,000 m
        window_x = self.position[0] * SCALE + 700
        window_y = self.position[1] * SCALE + 375
        pygame.draw.circle(window, self.color, (window_x, window_y), self.radius)