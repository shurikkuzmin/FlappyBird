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

clock = pygame.time.Clock()


WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
WINDOW.fill(BLACK)
FPS = 60
JUMP_FPS = 30

class Bird:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.y_bottom = 0
        self.y_top = 0
        self.surface = sprites.subsurface((380,185,20,20))
        self.surface = pygame.transform.scale(self.surface, (SCALE*20, SCALE*20))
        
    def lift(self):
        self.vel_y = -10.0
        self.acc_y = 0.0
        self.y_bottom = max(0, self.y + int(self.vel_y * JUMP_FPS))
    
    def update(self):
        self.x = self.x + int(self.vel_x)
        self.y = self.y + int(self.vel_y)
        self.vel_x = self.vel_x + self.acc_x
        self.vel_y = self.vel_y + self.acc_y
        
        if self.y < self.y_bottom:
            self.vel_y = 0.0
            self.acc_y = 0.7
            self.y = self.y_bottom
            self.y_bottom = 0
   
pygame.init()

bird1 = Bird(WIDTH/3, HEIGHT/2)
bird2 = Bird(WIDTH/4, HEIGHT*3/4)


isActive = True
while isActive:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird1.lift()
            if event.key == pygame.K_w:
                bird2.lift()
    bird1.update()
    bird2.update()

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_ESCAPE] == True:
        isActive = False
    clock.tick(FPS)
    
    WINDOW.blit(bird1.surface, (bird1.x, bird1.y))
    WINDOW.blit(bird2.surface, (bird2.x, bird2.y))
    pygame.display.update()
pygame.quit()

