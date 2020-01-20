import pygame
import random

from classes.config import Config

from classes.GameObject import GameObject


class Apple:
    def __init__(self, display):
        self.x_pos = 0
        self.y_pos = 0
        self.display = display
        self.randomize()

    def randomize(self):
        self.x_pos = random.randint(Config['front'],  Config['w_g'] - Config['front'] - Config['w_a'] )
        self.y_pos = random.randint(Config['front'], Config['h_g'] - Config['front'] - Config['h_a'])

    def draw(self):
        return pygame.draw.rect( self.display, Config ['col_dark'], [ self.x_pos, self.y_pos, Config['h_a'], Config['w_a'] ] )
