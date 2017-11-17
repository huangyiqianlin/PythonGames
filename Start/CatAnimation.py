import pygame, sys

pygame.init()

FPS = 1000  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
cat_x = 10
cat_y = 10
direction = 'right'

while True:
    DISPLAY_SURFACE.fill(WHITE)

    if direction == 'right':
        cat_x += 5
        if cat_x == 270:
            direction = 'down'
    elif direction == 'down':
        cat_y += 5
        if cat_y == 220:
            direction = 'left'
    elif direction == 'left':
        cat_x -= 5
        if cat_x == 10:
            direction = 'up'
    elif direction == 'up':
        cat_y -= 5
        if cat_y == 10:
            direction = 'right'

    DISPLAY_SURFACE.blit(catImg, (cat_x, cat_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
