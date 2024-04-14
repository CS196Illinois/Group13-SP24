import pygame
import sys
import math

pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.direction = pygame.math.Vector2()
        self.speed = 7

    def main(self, display):
        #Drawing Character
        pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

        #Movement
        self.input()
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed
		
    #Determining direction for movement
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
		
class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 15
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed
    
    def main(self, display):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(display, (0, 0, 0), (self.x, self.y), 5)


player = Player(400, 400, 32, 32)
player_bullets = []




while True:
    display.fill((54,54,86))

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_bullet = PlayerBullet(player.x, player.y, mouse_x, mouse_y)
                player_bullets.append(new_bullet)

    player.main(display)
    
    for bullet in player_bullets:
        bullet.main(display)




    
    

    clock.tick(60)
    pygame.display.update()