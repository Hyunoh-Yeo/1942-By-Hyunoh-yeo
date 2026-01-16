import pygame
import Enemy

class GroupEnemy:
    image = "Image/Enemy.png"
    
    def __init__(self, n):
        self.group = []

        for _ in range(n):
            self.group.append(Enemy(self.image))
