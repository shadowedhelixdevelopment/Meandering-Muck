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
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Meandering Muck")

    # Make a Slime.
    slime = Slime(ai_settings, screen)

    # Start main loop for the game.
    while True:
        gf.check_events(slime)
        slime.update()
        gf.update_screen(ai_settings, screen, slime)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
