import pygame
import Enemy

class GroupEnemy:
    image = "Image/Enemy.png"
    
    def __init__(self, n):
        self.group = []

        for _ in range(n):
            self.group.append(Enemy(self.image))

        self.count = n

        
    def move(self):
        return
    
    def display(self, screen):
        for enemy in self.group:
            screen.blit(enemy.image, (enemy.x, enemy. y))

    def checkCollision(self):
        def isCollision():
            return
        
        return

    def isDestroyed(self):
        return len(self.group) == 0
