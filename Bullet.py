import pygame

class Bullet:
    def __init__(self, image, playerX, playerY):
        self.image = pygame.image.load(image)

        self.x = playerX + 32
        self.y = playerY

        self.bullet_state = "ready"


