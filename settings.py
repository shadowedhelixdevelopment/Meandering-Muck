import pygame
import numpy
from numpy.random import randint as rand
import maze as mz


class Settings:
    """A class to store all settings for Meandering Muck"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (54, 38, 32)
        # Slime Settings.
        self.slime_speed_factor = 1.5
        # Maze Settings
        self.maze_width = 0
        self.maze_height = 0
        self.orig_bg = pygame.image.load("./images/stonefloor.gif")
        self.orig_stone = pygame.image.load("./images/stonetilefloor.gif")
        self.orig_slime = pygame.image.load('./images/slime.gif')
        self.orig_slime.set_colorkey((255, 255, 255))
        self.maze_block_width = None
        self.maze_block_height = None
        self.slime = None
        self.slime_width = None
        self.slime_height = None
        self.maze = None
        self.startx = None
        self.starty = None
        self.bg = None
        self.stone = None
        self.walls = []
        self.end = None
        self.loadnewsettings()

    def loadnewsettings(self):
        self.maze_width += 10
        self.maze_height += 10
        self.maze_block_width = self.screen_width / self.maze_width
        self.maze_block_height = self.screen_height / self.maze_height
        self.slime_width = self.maze_block_width / 2
        self.slime_height = self.maze_block_height / 2
        self.bg = pygame.transform.flip(self.orig_bg, bool(rand(0, 2)), bool(rand(0, 2)))
        self.stone = pygame.transform.scale(self.orig_stone, (int(self.maze_block_width), int(self.maze_block_height)))
        self.slime = pygame.transform.scale(self.orig_slime, (int(self.slime_width), int(self.slime_height)))
        self.generatenewmaze()

    def generatenewmaze(self):
        self.maze = mz.make_maze(self)
        for (x, y), value in numpy.ndenumerate(self.maze):
            if value == 2:
                self.startx = x
                self.starty = y
                break
        self.walls, self.end = mz.define_maze(self, self.maze)
