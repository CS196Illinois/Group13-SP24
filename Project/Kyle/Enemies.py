import pygame
from pygame.locals import*
import math
import random
from random import randrange
import sys

pygame.init()


display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Enemies')
BLACK = (255, 255, 255)

clock = pygame.time.Clock()
fps = 60

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.image = pygame.image.load('./img/blobLeft.png')
        self.base_player_image = self.image
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()


    def render(self, surface):
        surface.blit(self.image, self.pos)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            if self.pos.x > 0:
                self.pos.x -= 4
        if keys[K_RIGHT]:
            if self.pos.x < 800 - self.image.get_width():
                self.pos.x += 4
        if keys[K_DOWN]:
            if self.pos.y < 600 - self.image.get_height():
                self.pos.y += 3
        if keys[K_UP]:
            if self.pos.y > 0:
                self.pos.y -= 3

        self.hitbox_rect.center = self.pos

player = Player(400, 300)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
         self.image = pygame.image.load('./img/blueOrb.png').convert_alpha()
         # self.image = pygame.transform.rotozoom(self.image, 0, 2)
         self.rect = self.image.get_rect()
         self.rect.center = position
         self.direction = pygame.math.Vector2()
         self.vel = pygame.math.Vector2()
         self.speed = (random.random() * 2) + 1
        
         self.position = pygame.math.Vector2(position)

    def render(self, surface):
        surface.blit(self.image, self.position)

    def chase(self):
       player_vector = pygame.math.Vector2(player.hitbox_rect.center)
       enemy_vector = pygame.math.Vector2(self.rect.center)

       distance = self.get_distance(player_vector, enemy_vector)
       if distance > 0:
           self.direction = (player_vector - enemy_vector).normalize()
       else: 
           self.direction = pygame.math.Vector2()

       self.vel = self.direction * self.speed
       self.position += self.vel

       self.rect.centerx = self.position.x
       self.rect.centery = self.position.y

    def get_distance(self, vector1, vector2):
        return (vector1 - vector2).magnitude()
    
    def update(self):
        self.chase()

   


enemies = []

s_width, s_height = display.get_size()

enemy_spawnpoints = [(50, 50), (s_width - 50, 50), (50, s_height - 50), (s_width - 50, s_height - 50)]

# print(enemy_spawnpoints)

enemy_clock = 0
enemy_wait_time = random.randint(1, 7)

while True:

   enemy_clock += 1

   if enemy_clock >= enemy_wait_time * 60:
       enemy_clock = 0
       enemy_wait_time = random.randint(1, 7)
       start_pos = random.randint(0, 3)
       enemy = Enemy(enemy_spawnpoints[start_pos])
       enemies.append(enemy)

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
         pygame.QUIT

   player.move()


   display.fill(BLACK)

   for i in range(0,len(enemies)):
      enemies[i].update()
      enemies[i].render(display)

   player.render(display)
   clock.tick(fps)

   pygame.display.flip()
   




