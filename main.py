import sys
import pygame
from settings import Settings
from slime import Slime


def run_game():
    # Initialize pygame, settings and create screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Meandering Muck")

    # Make a Slime.
    slime = Slime(screen)

    # Start main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    slime.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


run_game()
