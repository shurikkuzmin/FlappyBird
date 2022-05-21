#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:00:20 2022

@author: shurik
"""
import pygame


PIPE_DISTANCE = 300
WIDTH = PIPE_DISTANCE*3
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
    def __init__(self, init_x, height, gap):
        self.x = init_x
        self.surf_top = sprites.subsurface((152,3,26,160))
        self.surf_bottom = sprites.subsurface((180,3,26,160))
        self.surf_top = pygame.transform.scale(self.surf_top, (SCALE*26, SCALE*160))
        self.surf_bottom = pygame.transform.scale(self.surf_bottom, (SCALE*26, SCALE*160))
        self.height = height
        self.gap = gap
        self.active = False
    
    def draw(self):
        WINDOW.blit(self.surf_top, (self.x,-SCALE*160+self.height))
        WINDOW.blit(self.surf_bottom, (self.x, self.height + self.gap))
    
    def update(self):
        if self.active == True:
            self.x = self.x - 2
            if self.x < -SCALE*26:
                self.x = WIDTH + PIPE_DISTANCE - SCALE*26
    
    def react_space(self):
        self.active = True

class Bird:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.acc_x = 0.0
        self.acc_y = 0.0
        self.surface = sprites.subsurface((380,185,20,20))
        self.surface = pygame.transform.scale(self.surface, (SCALE*20, SCALE*20))
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
    
    def draw(self):
        WINDOW.blit(self.surface, (self.x, self.y))
        
pygame.init()

bird = Bird(WIDTH/3, HEIGHT/2)
pipe1 = Pipe(WIDTH, 100, 175)
pipe2 = Pipe(WIDTH + PIPE_DISTANCE, 200, 175)
pipe3 = Pipe(WIDTH + 2*PIPE_DISTANCE, 150, 175)
pipe4 = Pipe(WIDTH + 3*PIPE_DISTANCE, 250, 175)

pipes = [pipe1, pipe2, pipe3, pipe4]
objects = [bird, pipe1, pipe2, pipe3, pipe4]

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
    
    bird.draw()
    pipe1.draw()
    pipe2.draw()
    pipe3.draw()
    pipe4.draw()
    
    
    pygame.display.update()
pygame.quit()

