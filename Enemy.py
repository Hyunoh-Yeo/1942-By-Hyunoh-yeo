import pygame
from Player import *

class Enemy(Player):
    destroyed = False
    attacked = False

    def move(self):
        if not self.destroyed:
            self.x += self.x_change
            self.y += self.y_change

            if self.x <= 0:
                self.x = 0
            elif self.x >= 1216:
                self.x = 1216

            if self.y >= 656:
                self.y = 656
                self.attacked = True