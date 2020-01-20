import pygame

from classes.config import Config
from classes.Game import Game


pygame.init()

display = pygame.display.set_mode((Config['w_g'], Config['h_g']))
pygame.display.set_caption('Project 3 semester by Iliya Puzhaev')


game = Game(display)

game.start_screen()



