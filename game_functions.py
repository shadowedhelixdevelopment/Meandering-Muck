import sys
import pygame


def check_events(play_button, slime):
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            slime.moving_right = True
        if event.key == pygame.K_LEFT or event.key == ord('a'):
            slime.moving_left = True
        if event.key == pygame.K_UP or event.key == ord('w'):
            slime.moving_top = True
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            slime.moving_down = True

    def check_keyup_events(event, slime):
        """Respond to key releases."""

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                slime.moving_right = False
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                slime.moving_left = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                slime.moving_top = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                slime.moving_down = False


def update_screen(ai_settings, screen, slime, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg, (0, 0))
    for i in range(0, len(ai_settings.walls)):
        wallrect = pygame.draw.rect(screen, (0, 0, 0), ai_settings.walls[i].rect)
        for k, v in sorted(ai_settings.stone.items(), reverse=True):
            screen.blit(v, wallrect)
            if i % k == 0:
                screen.blit(v, wallrect)
                break
    pygame.draw.rect(screen, (255, 255, 255), ai_settings.end.rect)
    slime.blitme()

    # Draw the play button if the game is inactive.
    if not game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
