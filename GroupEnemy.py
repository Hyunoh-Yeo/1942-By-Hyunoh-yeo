import pygame
from Enemy import *
import math
import random

class GroupEnemy:
    
    def __init__(self, n, image="Image/Enemy.png"):
        self.group = []

        self.x = random.randint(0, 1216 - (64 * n))
        self.y = 0

        self.image = image
        
        for i in range(n):
            self.group.append(Enemy(self.image, (self.x + (i * 64)), self.y))
        
    #move enemy until their terminate position
    def move(self, dx, dy):
        for enemy in self.group:
            enemy.move(dx, dy)
    
    #display undestroyed enemies
    def display(self, screen):
        for enemy in self.group:
            screen.blit(enemy.image, (enemy.x, enemy. y))

    #Check for collision and return score to be added
    def checkCollision(self, bullet):
        count = 0

        def isCollision(target, object):
            distance = math.sqrt(math.pow((target.x + 24) - object.x, 2) + math.pow(target.y - object.y, 2))

            if distance < 27:
                return True
            else:
                return False
            
        for enemy in self.group:
            if isCollision(enemy, bullet):
                self.group.remove(enemy)

                count += 1
        
        return count

    def isDestroyed(self):
        return len(self.group) == 0
    
    
    def checkAttacked(self):
        for enemy in self.group:
            if enemy.attacked:
                return True
        return False