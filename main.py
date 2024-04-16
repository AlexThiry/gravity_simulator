import pygame
from body import Body

#Initialize PyGame window

pygame.init()

windowSize = (1400,750)
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Gravity Simulator")
clock = pygame.time.Clock()

#Initialize bodies - UNITS: kg, m, m/s

sun = Body(1.989e30, [0,0], [0,0], 50, (255,255,0))
sun.center = True

earth = Body(5.98e24, [-1.496e11, 0], [0, 29784.8], 25, (0,0,255))
mars = Body(6.39e23, [208.41e9, 0], [0, -24.077 * 1000], 20, (255,0,0))
mercury = Body(3.3e23, [65.478e9, 0], [0, -47.4 * 1000], 10, (100,100,100))
venus = Body(4.8685e24, [-108.74e9, 0], [0, 35.02 * 1000], 15, (255,165,0))

moon = Body(7.3e22, [-1.496e11 - 384.4e6, 0], [0, 29784.8 + 1023.056], 5, (255,255,255))

bodiesToSimulate = [sun, earth, mars, mercury, venus, moon]

#Game function

def main():
    running = True
    dt = 3600 #1h timestep
    while running:
        clock.tick(120)
        window.fill((0,0,0))

        for body in bodiesToSimulate:
            body.updatePos(bodiesToSimulate, dt)
            body.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()

main()