import pygame
import random
import math
import os
from Player import *
from Enemy import *
from Bullet import *
from Button import *
from pygame import mixer
from GroupEnemy import *

os.chdir("1942-By-Hyunoh-yeo")

#Initializing pygame
pygame.init()

#Screen
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#Background
background = pygame.image.load("Image/Backgrounds.png").convert()
background_height = background.get_height()

tiles = math.ceil(screen_height / background_height) + 1
scroll = 0
d_scroll = 0.2

#Load Background Music
mixer.music.load("Sounds/Battlefield 1942 theme.wav")

#Start & Exir Button
startImg = pygame.image.load("Image/Start.png").convert_alpha()
exitImg = pygame.image.load("Image/Exit.png").convert_alpha()
start_button = Button(400, 150, startImg, 0.5)
exit_button = Button(500, 400, exitImg, 0.3)

#Title
title = "1942 by Hyunoh Yeo"
pygame.display.set_caption(title)

#Icon
icon = pygame.image.load("Image/Icon.png")
pygame.display.set_icon(icon)

#Sound Effects
bullet_sound = mixer.Sound("Sounds/Gun Sound.wav")
collision_sound = mixer.Sound("Sounds/explosion.wav")

#Shows score
def show_score(x, y):
    score = font.render("Score : " + str(score_val), True, (255, 255, 255))
    screen.blit(score, (x, y))

"""
#Check for collision between bullen and enemy
def isCollision(enemy, bullet):
    distance = math.sqrt(math.pow((enemy.x + 24) - bullet.x, 2) + math.pow(enemy.y - bullet.y, 2))

    if distance < 27:
        return True
    else:
        return False
"""

#Game Loop
running = True

#Game Status
menu = True
ingame = False
gameover = False
win = False

while running:
    if menu:
        while menu:
            screen.fill((0, 0, 0))

            if start_button.draw(screen):
                menu = False
                ingame = True

                continue

            if exit_button.draw(screen):
                running = False

                continue

            for event in pygame.event.get():

                #Check if Quitted
                if event.type == pygame.QUIT:
                    pygame.quit()     

            pygame.display.update()

    elif ingame:
        #Player
        playerImg = "Image/Player.png"
        player = Player(playerImg)

        #Group Enemy
        enemies = []
        enemies.append(GroupEnemy(random.randint(1, 5)))

        #Bullet
        bulletImg = "Image/Bullet.png"
        bullet = Bullet(bulletImg, 0, 800)
        bullets = []

        #Score
        score_val = 0
        font = pygame.font.Font("freesansbold.ttf", 32)
        textX = 10
        textY = 10

        #Play Background Music
        mixer.music.play(-1)

        play_time = 0
        while ingame:
            #RGB Screen
            screen.fill((80, 80, 250))

            #Background
            for i in range(tiles):
                screen.blit(background, (0, -((i * background_height)) + scroll))

            scroll += d_scroll
            if scroll > background_height:
                scroll = 0

            for event in pygame.event.get():

                #Check if Quitted
                if event.type == pygame.QUIT:
                    pygame.quit()

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
                        bulletImg = "Image/Bullet.png"
                        bullets.append(Bullet(bulletImg, 0, 800))

                        bullets[-1].fire(screen, player.x + 24, player.y)

                        bullet_sound.play()
                
                #Key Up
                if event.type == pygame.KEYUP:

                    #Arrow Released
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player.x_change = 0
                        player.y_change = 0

            #move player
            player.move()
            player.display(screen)

            #move each bullet from bullets list
            for thisbullet in bullets:
                if thisbullet.y < 0:
                    bullets.remove(thisbullet)
                else:
                    thisbullet.fire(screen, thisbullet.x, thisbullet.y)
                    thisbullet.y -= thisbullet.y_change

                for enemy in enemies:
                    score_add = enemy.checkCollision(thisbullet)

                    if score_add > 0:
                        bullets.remove(thisbullet)
                        score_val += score_add
                        collision_sound.play()

            #move enemies
            for enemy in enemies:
                enemy.move(0, 0.1)
                enemy.display(screen)

                if enemy.isDestroyed():
                    enemies.remove(enemy)

            if play_time > 0 and play_time % 3000 == 0:
                enemies.append(GroupEnemy(random.randint(1, 5)))

            if score_val >= 20:
                ingame = False
                win = True

            #display score
            show_score(textX, textY)

            pygame.display.update()

            play_time += 1

    elif win:
        while win:
            #RGB Screen
            screen.fill((80, 80, 250))

            #Background
            #screen.blit(background, (0, 0))

            #Game Over Text
            text = font.render("YOU WIN", True, (255, 255, 255))
            screen.blit(text, (550, 350))

            for event in pygame.event.get():

                #Check if Quitted
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()     

    elif gameover:
        while gameover:
            #RGB Screen
            screen.fill((80, 80, 250))

            #Background
            #screen.blit(background, (0, 0))

            #Game Over Text
            text = font.render("GAME OVER", True, (255, 255, 255))
            screen.blit(text, (550, 350))

            for event in pygame.event.get():

                #Check if Quitted
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()


#End Application      
pygame.quit()