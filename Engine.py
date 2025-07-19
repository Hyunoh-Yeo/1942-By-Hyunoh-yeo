import pygame
import random
import math
from Player import *
from Enemy import *
from Bullet import *
from pygame import mixer

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

#Score
score_val = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

#Background Sound
mixer.music.load("1942-By-Hyunoh-Yeo\Sounds\Battlefield 1942 theme.wav")
mixer.music.play(-1)

def show_score(x, y):
    score = font.render("Score : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

def isCollision(enemy, bullet):
    distance = math.sqrt(math.pow((enemy.x + 24) - bullet.x, 2) + math.pow(enemy.y - bullet.y, 2))

    if distance < 27:
        return True
    else:
        return False

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

    #move each bullet from bullets list
    for thisbullet in bullets:
        if thisbullet.y < 0:
            bullets.remove(thisbullet)
        else:
            thisbullet.fire(screen, thisbullet.x, thisbullet.y)
            thisbullet.y -= thisbullet.y_change

        if isCollision(enemy, thisbullet):
            enemy.destroyed = True
            mixer.music.load("1942-By-Hyunoh-Yeo\Sounds\explosion.wav")
            mixer.music.play(-1)

            score_val += 1

            bullets.remove(thisbullet)

    #move enemy
    if not enemy.destroyed and not enemy.attacked:
        enemy.display(screen)
    else:
        enemy = Enemy(enemyImg)

    #display score
    show_score(textX, textY)

    pygame.display.update()

#End Application      
pygame.quit()