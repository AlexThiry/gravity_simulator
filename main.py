import pygame
from body import Body
from functions import *

#Initialize PyGame window

pygame.init()

windowSize = (600,600)
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Gravity Simulator")
clock = pygame.time.Clock()

#Initialize bodies

sun = Body(1.989e30, [300,300], [0,0], 50, (255,255,0))
sun.center = True

earth = Body(5.98e24, [0,150], [1,0], 25, (0,0,255))

bodiesToSimulate = [sun, earth]

#Game function

def main():
    running = True
    while running:
        clock.tick(30)
        window.fill((0,0,0))
        sun.draw(window)
        earth.draw(window)

        f = getForceOfAttraction(sun.mass, earth.mass, getDistanceBetweenTwoBodies(sun.position, earth.position))
        sf = splitForceVector(f, sun.position, earth.position)
        earth.velocity = updateVelocity(earth.velocity, earth.mass, sf)


        earth.updatePos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()

main()