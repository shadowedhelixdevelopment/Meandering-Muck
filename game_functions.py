import sys

import pygame


def check_events(slime):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                slime.moving_right = True
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                slime.moving_left = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                slime.moving_up = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                slime.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                slime.moving_right = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                slime.moving_left = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                slime.moving_up = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                slime.moving_down = False


def update_screen(ai_settings, screen, slime):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    slime.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
