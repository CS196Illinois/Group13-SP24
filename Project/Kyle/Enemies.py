import pygame
from pygame.locals import*
import math
from random import randrange
import sys

pygame.init()

# goblin.draw(window)

# goblin = enemy(100, 410,  64, 64, 450)

display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Enemies')

clock = pygame.time.Clock()
fps = 60

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        # self.acc = vec(0, 0)
        # self.ACC = 1
        # self.FRIC = -0.1

        self.image = pygame.image.load('./img/blobLeft.png')


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

player = Player(400, 300)


class enemy(object):
   #  walkRight = [pygame.image.loadoad('x.png'), pygame.image.loadoad('x2.png'), pygame.image.loadoad('x3.png'), pygame.image.loadoad('x4.png')]
   #  walkLeft = [pygame.image.loadoad('y.png'), pygame.image.loadoad('y2.png'), pygame.image.loadoad('y3.png'), pygame.image.loadoad('y4.png')]
    
    def __init__(self, x, y, width, height, end):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.end = end
       self.path = [self.x, self.end]
       self.walkCount = 0
       self.vel = 3

    def draw(self, win):
       self.move()
       if self.walkCount + 1 >= 33:
          self.walkCount = 0

       if  self.vel > 0:
          win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
          self.walkCount += 1
       else:
          win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
          self.walkCount += 1


    def move(self):
       if self.vel > 0:
          if self.x + self.vel < self.path[1]:
             self.x += self.vel
          else:
             self.vel = self.vel * -1
             self.walkCount = 0
          if self.x - self.vel > self.path[0]:
             self.x += self.vel
          else:
             self.vel = self.vel * -1
             self.walkCount = 0

while True:

   

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()
         pygame.QUIT

   player.move()

   display.fill((255, 255, 255))
   player.render(display)
   clock.tick(fps)

   pygame.display.flip()
   




