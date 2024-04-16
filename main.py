import pygame
from body import Body
from functions import *

#1px = 10e6 km

pygame.init()

windowSize = (600,600)
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Gravity Simulator")

sun = Body(1.989e30, [300,300], [0,0], 50, (255,255,0))
earth = Body(5.98e24, [0,300], [0,0], 25, (0,0,255))

running = True

while running:
    window.fill((0,0,0))
    sun.draw(window)
    earth.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()