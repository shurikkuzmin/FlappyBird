#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:00:20 2022

@author: shurik
"""
import pygame

WIDTH = 600
HEIGHT = 800
SCALE = 4

BLACK = (0,0,0)


sprites = pygame.image.load("sprites.png")


bird = sprites.subsurface((380,185,20,20))
bird = pygame.transform.scale(bird, (SCALE*20, SCALE*20))
clock = pygame.time.Clock()

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
WINDOW.fill(BLACK)
FPS = 60
JUMP_FPS = 30

pygame.init()

bird_x = WIDTH/3
bird_y = HEIGHT/2
vel_y = 0
bird_y_barrier = 0
acc_y = 0

isActive = True
while isActive:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                vel_y = -5
                acc_y = 0
                bird_y_barrier = max(0, bird_y + vel_y * JUMP_FPS)
                #bird_y = bird_y - 20
    bird_y = bird_y + vel_y
    vel_y = vel_y + acc_y
    if bird_y < bird_y_barrier:
        vel_y = 0
        acc_y = 1
        bird_y = bird_y_barrier
        bird_y_barrier = 0

    keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE] == True:
    #    bird_y = bird_y - 20
    #    print("Space is pressed!!!")
        
    if keys[pygame.K_ESCAPE] == True:
        isActive = False
    clock.tick(FPS)
    
    WINDOW.blit(bird,(bird_x, bird_y))
    pygame.display.update()
pygame.quit()

