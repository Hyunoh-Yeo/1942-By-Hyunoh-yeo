import pygame
import random
from Player import *

class Enemy:
    destroyed = False
    attacked = False

    def __init__(self, image):
        self.image = pygame.image.load(image)

        self.x = random.randint(0, 1216)
        self.y = 0

        self.x_change = 0


    def move(self):
        if not self.destroyed:
            self.x += self.x_change
            self.y += 0.1

            if self.x <= 0:
                self.x = 0
            elif self.x >= 1216:
                self.x = 1216

            if self.y >= 656:
                self.y = 656
                self.attacked = True