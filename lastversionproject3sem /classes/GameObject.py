import pygame

from classes.config import Config

class GameObject :
    def __init__(self, x, y, display):
        self.x_pos = x
        self.y_pos = y
        self.size = 1
        self.display  = display
        self.body = [(self.x_pos, self.y_pos)]

    def update(self, dx, dy):
        self.body.append((self.x_pos, self.y_pos))
        self.x_pos += dx
        self.y_pos += dy
        if self.x_pos + Config['w_s'] > Config['w_g']:
            self.x_pos %= Config['w_g']
        if self.y_pos + Config['h_s'] > Config['h_g']:
            self.y_pos %= Config['h_g']
        if self.x_pos < 0:
            self.x_pos += Config['w_g']
        if self.y_pos < 0:
            self.y_pos += Config['h_g']

        if len(self.body) > self.size:
            del (self.body[0])













