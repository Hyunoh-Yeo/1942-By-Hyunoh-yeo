import pygame

class Player:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

        self.x_change = 0
        self.y_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

        if self.x <= 0:
            self.x = 0
        elif self.x >= 1216:
            self.x = 1216

        if self.y <= 0:
            self.y = 0
        elif self.y >= 656:
            self.y = 656

