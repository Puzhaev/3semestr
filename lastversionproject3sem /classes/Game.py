import pygame
from classes.snake import Snake
from classes.config import Config
from classes.apple import Apple
from classes.GameObject import GameObject
import random
import os


def load_image(name, color_key=None):
    fullname = os.path.join('materials', name)
    image = pygame.image.load(fullname)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image
        

class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0
        pygame.init()
        
        
    def start_screen(self):
        fon = pygame.transform.scale(load_image('snake.jpg'), (600, 600))
        self.display.blit(fon, (0, 0))
        while True:
            for j in pygame.event.get():
                if j.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif j.type == pygame.KEYDOWN or j.type == pygame.MOUSEBUTTONDOWN:
                    self.loop()
                    return
            pygame.display.flip()    
            

    def loop( self ):
        flag = False

        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.Font('materials/text.ttf', 25)

        title = font.render('Snake', True, Config['col_dark'])
        title_rect = title.get_rect( center=( Config ['w_g'] / 2, Config['front'] / 2 + 5) )
        
        file = open('materials/high_score.txt')
        high_score = int(file.readline())
        file.close()        

        pygame.mixer.music.load('materials/music.wav')
        pygame.mixer.music.play(-1)
        eat_apple = pygame.mixer.Sound('materials/sound.wav')

        snake = Snake( Config['w_g'] / 2, Config['h_g'] / 2, self.display )
        dx = 0
        dy = 0
        self.score = 0

        apple = Apple(self.display)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and dx != Config['sp']:
                        dx = -Config['sp']
                        dy = 0
                    elif event.key == pygame.K_RIGHT and dx != -Config['sp']:
                        dx = Config['sp']
                        dy = 0
                    elif event.key == pygame.K_UP and dy != Config['sp']:
                        dx = 0
                        dy = -Config['sp']
                    elif event.key == pygame.K_DOWN and dy != -Config['sp']:
                        dx = 0
                        dy = Config['sp']




            pygame.draw.rect(self.display, Config['col_light'], [0, 0, Config['h_g'], Config['w_g']])

            snake.update(dx, dy)
            snake_rect = snake.draw()
            apple_rect = apple.draw()


            if apple_rect.colliderect(snake_rect):
                apple.randomize()
                self.score += 1
                snake.eat()
                eat_apple.play()
            if len(snake.body) > 1:
                for cell in snake.body:
                    if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                        if self.score > high_score:
                            os.remove('materials/high_score.txt')
                            f = open('materials/high_score.txt', mode='w')
                            print(str(self.score), file=f)
                            f.close()
                        self.loop()

            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, Config['col_dark'])
            
            high_score_text = 'High score: {}'.format(str(high_score))
            high_score_font = font.render(high_score_text, True, Config['col_dark'])            

            score_rect = score.get_rect( center=(Config['score_x'], Config['h_g'] - Config['front'] / 2 - 30) )
            high_score_rect = high_score_font.get_rect( center=( Config['high_x'], Config['h_g'] - Config['front'] / 2 - 5) )

            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)
            self.display.blit(high_score_font, high_score_rect)

            pygame.display.update()

            if flag:
                if self.score > high_score:
                    os.remove('data/high_score.txt')
                    f = open('data/high_score.txt', mode='w')
                    print(str(self.score), file=f)
                    f.close()
                self.loop()


            clock.tick_busy_loop(Config['fps'])










