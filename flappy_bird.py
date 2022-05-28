#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:00:20 2022

@author: shurik
"""
import pygame
import random


PIPE_DISTANCE = 300
NUM_PIPES = 4
WIDTH = PIPE_DISTANCE*(NUM_PIPES - 1)
HEIGHT = 800
SCALE = 4

BLACK = (0,0,0)


sprites = pygame.image.load("sprites.png")

clock = pygame.time.Clock()


WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
WINDOW.fill(BLACK)
FPS = 60
JUMP_FPS = 6

class Pipe:
    def __init__(self, init_x, gap):
        self.surf_top = sprites.subsurface((152,3,26,160))
        self.surf_bottom = sprites.subsurface((180,3,26,160))
        self.surf_top = pygame.transform.scale(self.surf_top, (SCALE*26, SCALE*160))
        self.surf_bottom = pygame.transform.scale(self.surf_bottom, (SCALE*26, SCALE*160))
        self.height = random.randint(50,HEIGHT-50-gap)
        self.gap = gap
        self.rect_top = self.surf_top.get_rect()
        self.rect_bottom = self.surf_bottom.get_rect()
        self.rect_top.left = init_x
        self.rect_top.bottom = self.height
        self.rect_bottom.left = init_x
        self.rect_bottom.top = self.height + self.gap
        self.active = False
    
    def draw(self):
        WINDOW.blit(self.surf_top, self.rect_top)
        WINDOW.blit(self.surf_bottom, self.rect_bottom)
    
    def update(self):
        if self.active == True:
            self.rect_top.left = self.rect_top.left - 2
            self.rect_bottom.left = self.rect_bottom.left - 2
            
            if self.rect_top.right < 0:
                self.rect_top.right = WIDTH + PIPE_DISTANCE
                self.rect_bottom.right = WIDTH + PIPE_DISTANCE                
                self.height = random.randint(50,HEIGHT - 50 - self.gap)
    
    def react_space(self):
        self.active = True

class Bird:
    def __init__(self, init_x, init_y):
        #self.x = init_x
        #self.y = init_y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.surface = sprites.subsurface((380,185,20,20))
        self.surface = pygame.transform.scale(self.surface, (SCALE*20, SCALE*20))
        self.rect = self.surface.get_rect()
        self.rect.left = init_x
        self.rect.top = init_y
        self.state = 0 # Neutral state
        
        
    def react_space(self):
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
        if self.rect.top < 0:
            self.rect.top = 0
            self.state = 2
            self.update_state()
        
            
    def update(self):
        self.rect.left = self.rect.left + int(self.vel_x)
        self.rect.top = self.rect.top + int(self.vel_y)
        self.vel_x = self.vel_x + self.acc_x
        self.vel_y = self.vel_y + self.acc_y
        
        self.check_state()
    
    def draw(self):
        WINDOW.blit(self.surface, self.rect)
    
    def check_obstacles(self, pipes):
        collision = False
        for pipe in pipes:
            collision = bird.rect.colliderect(pipe.rect_bottom)
            if collision == True:
                break
            collision = bird.rect.colliderect(pipe.rect_top)
            if collision == True:
                break
        if collision:
            self.state = 0
            self.update_state()
pygame.init()

bird = Bird(WIDTH/3, HEIGHT/2)
objects = [bird]
pipes = []

for i in range(NUM_PIPES):
    pipe = Pipe(WIDTH + i * PIPE_DISTANCE,250)
    objects.append(pipe)
    pipes.append(pipe)

isActive = True
while isActive:
    WINDOW.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isActive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for obj in objects:
                    obj.react_space()
    
    for obj in objects:
        obj.update()

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_ESCAPE] == True:
        isActive = False
    clock.tick(FPS)
    
    for obj in objects:
        obj.draw()
    
    bird.check_obstacles(pipes)
        
    pygame.display.update()
    
pygame.quit()

