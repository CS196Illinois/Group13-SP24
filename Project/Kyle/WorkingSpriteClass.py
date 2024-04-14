import pygame
from pygame.locals import *

fps = 60
clock = pygame.time.Clock()

window_size = (800, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Moving Blob')


vec = pygame.math.Vector2

rect_1 = pygame.Rect(0, 0, 800, 50)
rect_2 = pygame.Rect(750, 50, 50, 550)
rect_3 = pygame.Rect(0, 50, 50, 550)
rect_4 = pygame.Rect(50, 550, 700, 50)
background = pygame.Rect(50, 50, 700, 500)



# Creating the class to load sprites
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
            if self.pos.x > 50:
                self.pos.x -= 4
        if keys[K_RIGHT]:
            if self.pos.x < 750 - self.image.get_width():
                self.pos.x += 4
        if keys[K_DOWN]:
            if self.pos.y < 550 - self.image.get_height():
                self.pos.y += 3
        if keys[K_UP]:
            if self.pos.y > 50:
                self.pos.y -= 3

player = Player(400, 300)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Background needs to be reloaded in between each movement so the previous blit disappears
    player.move()
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 102, 102), rect_1)
    pygame.draw.rect(window, (0, 102, 102), rect_2)
    pygame.draw.rect(window, (0, 102, 102), rect_3)
    pygame.draw.rect(window, (0, 102, 102), rect_4)
    pygame.draw.rect(window, (153, 0, 76), background)
    # world.draw()
    player.render(window)
    
    pygame.display.flip()
    clock.tick(fps)