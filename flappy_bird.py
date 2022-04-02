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

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
WINDOW.fill(BLACK)

pygame.init()

isActive = True
while isActive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
    WINDOW.blit(bird,(WIDTH/3,HEIGHT/2))
    pygame.display.update()
pygame.quit()

