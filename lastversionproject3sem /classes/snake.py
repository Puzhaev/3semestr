import pygame

from classes.config import Config

from classes.GameObject import GameObject

class Snake ( GameObject ):
    def eat(self):
        self.size += 1
    def draw(self):
        for i in range(len(self.body)):
            tmp_rect = pygame.draw.rect(self.display, Config['col_dark'], [ self.body[i][0], self.body[i][1], Config['w_s'], Config['h_s'] ])
        return tmp_rect








