import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game vars
tile_size = 200

#load images
bg_img = pygame.image.load('img/sky.jpg')

class World():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt_img = pygame.image.load('img/darkDirtBlock.png')
        grass_img = pygame.image.load('img/darkGrassDirtBlock.png')
        row_count = 0
        for row in data:
            for tile in row:
                col_count = 0
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

                
    def draw(self):
        for tile in self.tile_list:
            screen.blit('./img/darkDirtBlock.png', tile)


world_data = [
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 2, 2, 2, 1],
]

world = World(world_data)


run = True
while run:

    # screen.blit(bg_img, (0, 0))

    world.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()