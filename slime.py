import pygame


class Slime():

    def __init__(self, screen):
        """Initialize the slime and set it's starting position."""
        self.screen = screen

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen(Will change later).
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        def blitme(self):
            """Draw the slime at it's current location."""
            self.screen.blit(self.image, self.rect)
