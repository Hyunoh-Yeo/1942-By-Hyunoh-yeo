import pygame

class Button:
    def __init__(self, x, y, image, scale):
        #Set scale of the image
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

        #give the rectangular surface to the image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked = False

    def draw(self, screen):
        #get click action
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        #If clicked released, able clicking
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action