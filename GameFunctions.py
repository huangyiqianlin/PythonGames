import pygame
import sys
import random


def game_over():
    pygame.quit()
    sys.exit()


def call(function):
    return function()


def get_randomized_board(settings):
    """ 生成icon的排列组合 数据结构 """
    icons = []
    for color in settings.all_colors:
        for shape in settings.all_shapes:
            icons.append((shape, color))

    random.shuffle(icons)  # randomize the order of the icons list
    num_icons_used = int(settings.board_width * settings.board_height / 2)  # calculate how many icons are needed
    icons = icons[:num_icons_used] * 2  # make two of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(settings.board_width):
        column = []
        for y in range(settings.board_height):
            column.append(icons[0])
            del icons[0]  # remove the icons as we assign them
        board.append(column)
    return board


def generate_revealed_boxes_data(settings, val):
    """ 生成方块是否被翻开的数据矩阵结构 """
    revealed_boxes = []
    for i in range(settings.board_width):
        revealed_boxes.append([val] * settings.board_height)
    return revealed_boxes
