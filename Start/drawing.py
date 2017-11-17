import pygame, sys

pygame.init()

# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAY_SURFACE.fill(WHITE)

# 多边形
pygame.draw.polygon(DISPLAY_SURFACE, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

pygame.draw.line(DISPLAY_SURFACE, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAY_SURFACE, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAY_SURFACE, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAY_SURFACE, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAY_SURFACE, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAY_SURFACE, RED, (200, 250, 100, 50))

pixObj = pygame.PixelArray(DISPLAY_SURFACE)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()