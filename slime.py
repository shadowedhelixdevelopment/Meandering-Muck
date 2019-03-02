import pygame


class Slime():

    def __init__(self, screen):
        """Initialize the slime and set it's starting position."""
        self.screen = screen

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('./images/slimetop2.50.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen(Will change later).
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the slime's center value, not the rect.
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        if self.moving_up:
            self.rect.centery -= 1
        if self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        """Draw the slime at it's current location."""
        self.screen.blit(self.image, self.rect)
