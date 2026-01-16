import pygame

class Player:
    def __init__(self, image):
        self.image = pygame.image.load(image)

        #Create Player in the Middle
        self.x = 608
        self.y = 650

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

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

