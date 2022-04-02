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

pygame.init()

bird_x = WIDTH/3
bird_y = HEIGHT/2

isActive = True
while isActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        bird_y = bird_y - 20
        print("Space is pressed!!!")
        
    if keys[pygame.K_ESCAPE] == True:
        isActive = False
    clock.tick(FPS)
    
    WINDOW.blit(bird,(bird_x, bird_y))
    pygame.display.update()
pygame.quit()

