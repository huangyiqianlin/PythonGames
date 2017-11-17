import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('hehe')

FPS = 5

bg_color = (244, 233, 222)

screen.fill((255, 255, 255))
clock = pygame.time.Clock()


def main():
    i = 1
    while i < 100:
        screen.fill((255, 255, 255))

        rect = pygame.Rect(100 + i, 100 + i, 100, 100)
        pygame.draw.rect(screen, bg_color, rect)

        another_rect = pygame.Rect(10 + i, 10 + i, 50, 50)
        pygame.draw.rect(screen, bg_color, another_rect)

        i += 1
        
        pygame.display.update()
        clock.tick(FPS)
        pygame.event.get()

        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS)"""


main()
