import pygame
import pygame.mixer
import sys
import math

pygame.init()

#for music
pygame.mixer.init()
pygame.mixer.music.load('./graphics/lofi.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #commenting it out since sprite implementation
        #self.width = width
        #self.height = height
        self.direction = pygame.math.Vector2()
        self.speed = 7
        self.image = pygame.image.load('./graphics/player.png') #for implementing sprites

    def main(self): 
        #Drawing Character - commenting it out since sprite implementation
        #pygame.draw.rect(display, (255, 0, 0), (self.x, self.y, self.width, self.height))

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

    def render(self, surface): #function for implementing sprites
        surface.blit(self.image, self.direction)
		
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


player = Player(400, 400)
player_bullets = []

while True:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                new_bullet = PlayerBullet(player.x, player.y, mouse_x, mouse_y)
                player_bullets.append(new_bullet)
    
    background = pygame.image.load('./graphics/background.jpg') #for bg

    display.fill((255,255,255))
    display.blit(background, (0, 0)) #adding sprite bg
    player.render(display)
    player.main()
    
    for bullet in player_bullets:
        bullet.main(display)

    clock.tick(60)
    #pygame.display.update() commented out since background needs to be reloaded in between each movement so the previous blit disappears
    pygame.display.flip()