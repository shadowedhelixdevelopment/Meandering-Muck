import sys
import pygame
from settings import Settings
from slime import Slime
import game_functions as gf
import maze as mz
import numpy


def run_game():
    # Initialize pygame, settings and create screen object.
    pygame.init()
    maze = mz.make_maze()
    ai_settings = Settings()
    for (x, y), value in numpy.ndenumerate(maze):
        if value == 2:
            startx = x
            starty = y
            break
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Meandering Muck")

    # Make a Slime.
    slime = Slime(ai_settings, screen, startx, starty)

    # Start main loop for the game.
    while True:
        gf.check_events(slime)
        slime.update()
        gf.update_screen(ai_settings, screen, maze, slime)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
