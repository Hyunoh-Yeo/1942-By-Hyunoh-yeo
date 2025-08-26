import pygame
import random
from Player import *

class Enemy:
    destroyed = False
    attacked = False

    def __init__(self, image, x=-1, y=-1):
        self.image = pygame.image.load(image)

        if x == -1:
            self.x = random.randint(0, 1216)
        else:
            self.x = x
        
        if y == -1:
            self.y = 0
        else:
            self.y = 0

        """
        self.x_change = 0.5
        """

    def move(self, dx, dy):
        if not self.destroyed:
            """
            self.x += self.x_change
            """
            self.x += dx
            self.y += dy

            """
            if self.x <= random.randint(0, 1216): #방향 바뀌는 interval 이 너무 짧음 
                self.x_change = 0.5
            elif self.x >= random.randint(0, 1216):
                self.x_change = -0.5
            """

            if self.y >= 656:
                self.y = 656
                self.attacked = True

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))