import pygame, sys

pygame.init()
DISPLAY_SURFACE = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello World!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

# run the game loop
while True:
    DISPLAY_SURFACE.fill(WHITE)
    DISPLAY_SURFACE.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
