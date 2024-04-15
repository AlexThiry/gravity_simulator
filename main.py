import pygame
from body import Body
from math import sqrt

pygame.init()

windowSize = (600,600)
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Gravity Simulator")

sun = Body(1.989e30,[300,300],[0,0],50,(255,255,0))

running = True

while running:
    window.fill((0,0,0))
    sun.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()