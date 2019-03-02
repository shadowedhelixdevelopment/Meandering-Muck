import pygame


class Slime():

    def __init__(self, ai_settings, screen, x, y):
        """Initialize the slime and set it's starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('./images/slime.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the entrance to the maze.
        print(x, y)
        if x == 0:
            self.rect.left = 0
        elif x == ai_settings.maze_width - 1:
            self.rect.right = ai_settings.screen_width
        else:
            self.rect.centerx = x * ai_settings.maze_block_width + (ai_settings.maze_block_width / 2)
        if y == 0:
            self.rect.top = 0
        elif y == ai_settings.maze_height - 1:
            self.rect.bottom = ai_settings.screen_height
        else:
            self.rect.centery = y * ai_settings.maze_block_height + (ai_settings.maze_block_height / 2)

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the slime's center value, not the rect.
        if self.moving_right:
            self.centerx += self.ai_settings.slime_speed_factor
        if self.moving_left:
            self.centerx -= self.ai_settings.slime_speed_factor
        if self.moving_up:
            self.centery -= self.ai_settings.slime_speed_factor
        if self.moving_down:
            self.centery += self.ai_settings.slime_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the slime at it's current location."""
        self.screen.blit(self.image, self.rect)
