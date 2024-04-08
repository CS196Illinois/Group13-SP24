import pygame
import sys
import math
from random import randrange

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Enemies')


zombiex = randrange(800)
zombiey = randrange(600)
zombiespeed = 4

def add_zombie_at_location(x, y):
    game_display.blit(zombie)


while True:

    display.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
