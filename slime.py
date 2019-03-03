import pygame


class Slime():

    def __init__(self, ai_settings, screen, x, y, walls):
        """Initialize the slime and set it's starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.walls = walls

        # Load the ship image and get it's rect.
        self.image = pygame.image.load('./images/slime.gif')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the entrance to the maze.
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
        self.moving_top = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        collidebottom = 0
        collidetop = 0
        collideright = 0
        collideleft = 0
        # Update the slime's center value, not the rect.
        for i in range(0, len(self.walls)):
            if self.rect.colliderect(self.walls[i].rect):
                if self.rect.bottom > self.walls[i].rect.top:
                    if self.rect.bottom - self.walls[i].rect.top <= 2:
                        collidebottom = 1
                if self.rect.top < self.walls[i].rect.bottom:
                    if self.walls[i].rect.bottom - self.rect.top <= 2:
                        collidetop = 1
                if self.rect.right > self.walls[i].rect.left:
                    if self.rect.right - self.walls[i].rect.left <= 2:
                        collideright = 1
                if self.rect.left < self.walls[i].rect.right:
                    if self.walls[i].rect.right - self.rect.left <= 2:
                        collideleft = 1
        if self.moving_right and self.rect.right < self.screen_rect.right and collideright != 1:
            self.centerx += self.ai_settings.slime_speed_factor
        if self.moving_left and self.rect.left > 0 and collideleft != 1:
            self.centerx -= self.ai_settings.slime_speed_factor
        if self.moving_top and self.rect.top > self.screen_rect.top and collidetop != 1:
            self.centery -= self.ai_settings.slime_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom and collidebottom != 1:
            self.centery += self.ai_settings.slime_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the slime at it's current location."""
        self.screen.blit(self.image, self.rect)
