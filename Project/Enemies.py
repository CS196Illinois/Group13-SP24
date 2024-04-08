import pygame
pygame.init()

goblin.draw(window)

goblin = enemy(100, 410,  64, 64, 450)


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
        else:
          if self.x - self.vel > self.path[0]:
             self.x += self.vel
          else:
             self.vel = self.vel * -1
             self.walkCount = 0:


