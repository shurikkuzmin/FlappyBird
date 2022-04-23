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
        #self.y_bottom = 0
        #self.y_top = 0
        self.surface = sprites.subsurface((380,185,20,20))
        self.surface = pygame.transform.scale(self.surface, (SCALE*20, SCALE*20))
        self.state = 0 # Neutral state
        
        
    def lift(self):
        self.state = 1 # Lift state
        self.update_state()

    def update_state(self):
        if self.state == 0:
            self.vel_y = 0.0
            self.acc_y = 0.0
            self.counter_lift = 0
        if self.state == 1:
            self.vel_y = -10.0
            self.acc_y = 0.0
            self.counter_lift = 0
        if self.state == 2:
            self.counter_lift = 0
            self.vel_y = 0.0
            self.acc_y = 0.7
        
    def check_state(self):
        if self.state == 1:
            self.counter_lift = self.counter_lift + 1
            if self.counter_lift > JUMP_FPS:
                self.state = 2
                self.update_state()
        if self.y < 0:
            self.y = 0
            self.state = 2
            self.update_state()
        
            
    def update(self):
        self.x = self.x + int(self.vel_x)
        self.y = self.y + int(self.vel_y)
        self.vel_x = self.vel_x + self.acc_x
        self.vel_y = self.vel_y + self.acc_y
        
        self.check_state()
   
pygame.init()

bird = Bird(WIDTH/3, HEIGHT/2)

isActive = True
while isActive:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.lift()
    bird.update()

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_ESCAPE] == True:
        isActive = False
    clock.tick(FPS)
    
    WINDOW.blit(bird.surface, (bird.x, bird.y))
    pygame.display.update()
pygame.quit()

