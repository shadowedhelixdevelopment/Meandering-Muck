import pygame
from settings import Settings

class Wall():
    def __init__(self, x, y):
        ai_settings = Settings()
        self.rect = pygame.Rect(x, y, ai_settings.maze_block_width, ai_settings.maze_block_height)