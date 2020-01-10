import pygame
from classes.snake import Snake
from classes.config import Config
from classes.apple import Apple
from classes.GameObject import GameObject

class Game:
    def __init__(self, display):
        self.display = display
        self.score = 0
        pygame.init()

    def loop( self ):
        flag = False

        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.Font('materials/text.otf', 25)

        title = font.render('Snake', True, Config['col_w'])
        title_rect = title.get_rect( center=( Config ['w_g'] / 2, Config['front'] / 2) )

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
                    exit()
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

                print(event)



            pygame.draw.rect(self.display, Config['col_b'], [0, 0, Config['h_g'], Config['w_g']])

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
                        self.loop()

            score_text = 'Score: {}'.format(self.score)
            score = font.render(score_text, True, Config['col_w'])

            score_rect = score.get_rect( center=( Config['w_g'] / 2, Config['h_g'] - Config['front'] / 2) )

            self.display.blit(score, score_rect)
            self.display.blit(title, title_rect)

            pygame.display.update()

            if flag:
                self.loop()


            clock.tick_busy_loop(Config['fps'])










