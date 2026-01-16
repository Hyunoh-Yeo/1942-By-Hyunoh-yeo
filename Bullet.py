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

        mixer.music.load("1942-By-Hyunoh-Yeo\Sounds\Gun Sound.wav")
        mixer.music.play(-1)

        screen.blit(self.image, (x, y))

 