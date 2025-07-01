import pygame

#Initializing pygame
pygame.init()

#Screen
screen = pygame.display.set_mode((1280, 720))

#Title
title = "1942 by Hyunoh Yeo"
pygame.display.set_caption(title)

#Icon
icon = pygame.image.load(".\Image\Icon.png")
pygame.display.set_icon(icon)

#Game Loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB Screen
    screen.fill((250, 250, 250))
    pygame.display.update()

#End Application      
pygame.quit()