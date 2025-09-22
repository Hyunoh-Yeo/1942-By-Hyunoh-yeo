import pygame
from pygame import mixer

class Bullet:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)

        self.x = x
        self.y = y
        self.y_change = 1
    def fire(self, screen, x, y):
        self.x = x
        self.y = y

        screen.blit(self.image, (x, y))

 