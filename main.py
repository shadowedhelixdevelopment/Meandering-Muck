import pygame
from settings import Settings
from slime import Slime
from Button import Button
import game_functions as gf


def run_game():
    # Initialize pygame, settings and create screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Meandering Muck")

    # Make the play_button
    play_button = Button(ai_settings, screen, "Begin")
    # Make a Slime.
    slime = Slime(ai_settings, screen)

    # Start main loop for the game.
    while True:
        gf.check_events(play_button, slime)
        slime.update()
        gf.update_screen(ai_settings, screen, slime, play_button)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
