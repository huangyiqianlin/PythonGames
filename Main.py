import pygame
import random
import sys
from Settings import Settings
from Loop import Loop
import GameFunctions

pygame.init()

settings = Settings()
screen = pygame.display.set_mode((settings.window_width, settings.window_height))
pygame.display.set_caption('Memory Puzzle')

loop = Loop()
loop.register_events(pygame.QUIT, GameFunctions.game_over)

mouse_x = 0
mouse_y = 0

main_board = get_randomized_board()
revealed_boxes = generate_revealed_boxes_data(False)

first_selection = None  # stores the (x, y) of the first box clicked.

while True:
    screen.fill(settings.bg_color)
    loop.run()
    pygame.display.update()
