import pygame

class Bullet:
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)

        self.x = x
        self.y = y
        self.y_change = 0.5

        self.bullet_state = "ready"

    def fire(self, screen, x, y):
        self.bullet_state = "fire"

        self.x = x
        self.y = y

        screen.blit(self.image, (x, y))

 