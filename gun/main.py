import pygame
import sys
from gun import gun

WHITE=(0, 255, 0)
black=(0,0,0)

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Game of zohan')
    bgc=(0,0,0)
    bgc1=(0,255,0)
    clock=pygame.time.Clock()

    g=gun(screen)
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                # sys.exit()
                running=False

        screen.fill(bgc)
        g.upd()
        g.output()
        """
        sc=screen
        pygame.draw.line(sc, WHITE,
                         [10, 30],
                         [290, 15], 7)
        pygame.draw.line(sc, WHITE,
                         [10, 50],
                         [290, 35])
        pygame.draw.aaline(sc, WHITE,
                           [10, 70],
                           [290, 55])


        """
        pygame.display.flip()
        clock.tick(30) #FPS


run()