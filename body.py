import pygame

class Body():
    def __init__(self, mass, position, velocity, radius, color) -> None:
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color
    def updatePos(self):
        self.position += self.velocity
    def draw(self, d):
        pygame.draw.circle(d, self.color, self.position, self.radius)