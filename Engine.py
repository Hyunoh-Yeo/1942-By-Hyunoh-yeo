import pygame
import random
from Player import *
from Enemy import *
from Bullet import *

#Initializing pygame
pygame.init()

#Screen
screen = pygame.display.set_mode((1280, 720))

#Background
background = pygame.image.load("1942-By-Hyunoh-yeo\Image\Background.png")

#Title
title = "1942 by Hyunoh Yeo"
pygame.display.set_caption(title)

#Icon
icon = pygame.image.load("1942-By-Hyunoh-Yeo\Image\Icon.png")
pygame.display.set_icon(icon)

#Player
playerImg = "1942-By-Hyunoh-Yeo\Image\Player.png"
player = Player(playerImg)

#Enemy
enemyImg = "1942-By-Hyunoh-Yeo\Image\Enemy.png"
enemy = Enemy(enemyImg)

#Bullet
bulletImg = "1942-By-Hyunoh-Yeo\Image\Bullet.png"
bullet = Bullet(bulletImg, 0, 800)
bullets = []

#Game Loop
running = True
while running:

    #RGB Screen
    screen.fill((250, 250, 250))

    #Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        #Check if Quitted
        if event.type == pygame.QUIT:
            running = False

        #Key Down
        if event.type == pygame.KEYDOWN:
            
            #Arrow Pressed
            if event.key == pygame.K_LEFT:
                player.x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player.x_change = 0.5
            if event.key == pygame.K_UP:
                player.y_change = -0.5
            if event.key == pygame.K_DOWN:
                player.y_change = 0.5

            #Space Pressed
            if event.key == pygame.K_SPACE:
                bulletImg = "1942-By-Hyunoh-Yeo\Image\Bullet.png"
                bullets.append(Bullet(bulletImg, 0, 800))

                bullets[-1].fire(screen, player.x + 24, player.y)

        
        #Key Up
        if event.type == pygame.KEYUP:

            #Arrow Released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.x_change = 0
                player.y_change = 0

    #move player
    player.move()
    enemy.move()
    player.display(screen)

    #move enemy
    if not enemy.destroyed and not enemy.attacked:
        enemy.display(screen)
    else:
        enemy = Enemy(enemyImg)

    #move each bullet from bullets list
    for thisbullet in bullets:
        if thisbullet.y < 0:
            bullets.remove(thisbullet)
        if thisbullet.bullet_state is "fire":
            thisbullet.fire(screen, thisbullet.x, thisbullet.y)
            thisbullet.y -= thisbullet.y_change

    pygame.display.update()

#End Application      
pygame.quit()