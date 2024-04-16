import pygame
from body import Body

#Initialize PyGame window

pygame.init()

windowSize = (600,600)
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Gravity Simulator")
clock = pygame.time.Clock()

#Initialize bodies

sun = Body(1.989e30, [0,0], [0,0], 50, (255,255,0))
sun.center = True

earth = Body(5.98e24, [-1.496e11,0], [0, 29784.8], 25, (0,0,255)) #In meters
mars = Body(6.39e23, [208.41e9,0], [0, -24.077 * 1000], 20, (255,0,0))
mercury = Body(3.3e23, [65.478e9,0], [0, -47.4 * 1000], 10,(120,120,120))
venus = Body(4.8685e24, [-108.74e9, 0], [0, 35.02 * 1000], 15, (255,255,255))

bodiesToSimulate = [sun, earth, mars, mercury, venus]

#Game function

def main():
    running = True
    while running:
        clock.tick(60)
        window.fill((0,0,0))

        for body in bodiesToSimulate:
            body.updatePos(bodiesToSimulate)
            body.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()

main()