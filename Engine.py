import pygame
from Player import *

#Initializing pygame
pygame.init()

#Screen
screen = pygame.display.set_mode((1280, 720))

#Title
title = "1942 by Hyunoh Yeo"
pygame.display.set_caption(title)

#Icon
icon = pygame.image.load("1942-By-Hyunoh-Yeo\Image\Icon.png")
pygame.display.set_icon(icon)

#Player
playerImg = "1942-By-Hyunoh-Yeo\Image\F-22.png"
playerX = 608
playerY = 650

player = Player(playerImg, playerX, playerY)

def displayPlayer(temp):
    screen.blit(temp.image, (temp.x, temp.y))

#Game Loop
running = True
while running:

    #RGB Screen
    screen.fill((250, 250, 250))

    for event in pygame.event.get():

        #Check if Quitted
        if event.type == pygame.QUIT:
            running = False

        #Arrow Key Pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.x_change = -0.2
            if event.key == pygame.K_RIGHT:
                player.x_change = 0.2
            if event.key == pygame.K_UP:
                player.y_change = -0.2
            if event.key == pygame.K_DOWN:
                player.y_change = 0.2
        if event.type == pygame.KEYUP:
            player.x_change = 0
            player.y_change = 0

    #move player
    player.move()
    displayPlayer(player)

    pygame.display.update()

#End Application      
pygame.quit()