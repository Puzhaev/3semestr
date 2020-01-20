import pygame
import random


class Particle(pygame.sprite.Sprite):
    fire = [(255, 0, 0), (0, 200, 0), (0, 0, 255), (0, 200, 200), (255, 0, 255), (200, 200, 0)]

    def __init__(self, pos, dx, dy):
        super().__init__(particles)
        self.image = pygame.Surface((4, 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, random.choice(self.fire), (2, 2), 2)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = 0.1

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += int(self.velocity[0])
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()