import pygame, sys, math
import random
from random import randrange
from pygame.locals import*

pygame.mixer.init()
pygame.mixer.music.load('./graphics/lofi.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)


#defining classes
class StaticObstacle(pygame.sprite.Sprite):
    def __init__(self,pos,size,groups,color):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,obstacles,x,y):
        super().__init__(groups)
        #image
        self.image = pygame.Surface((30,60))
        self.image.fill('blue')
        self.obstacles = obstacles
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.image = pygame.image.load('./graphics/pumpkin.png')
        # self.image = pygame.transform.rotozoom(self.image, 0, 1)
        self.base_player_image = self.image
        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect = self.hitbox_rect.copy()

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        #movement input
        if keys[pygame.K_s]:
            self.direction.y = 1
        elif keys[pygame.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def collisions(self,direction):
        self.obstacles = pygame.sprite.spritecollide(self,collision_sprites,False)
        for sprite in self.obstacles:
            if direction == 'horizontal':
                #player moving right and colliding w sprite's left side
                if self.rect.right >= sprite.rect.left and self.old_rect.right >= sprite.rect.left:
                    self.rect.right = sprite.rect.left
                    self.pos.x = self.rect.x
                    self.direction.x *= -1


                #player moving left and colliding w sprite's right side
                if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.rect.right:
                    self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x
                    self.direction.x *= -1


            if direction == 'vertical':
                #player moving down and colliding w sprite's top
                if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.rect.top:
                    self.rect.bottom = sprite.rect.top
                    self.pos.y = self.rect.y
                    self.direction.y *= -1

                #player moving up and colliding w sprite's bottom
                if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.rect.bottom:
                    self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.direction.y *= -1


    def bordercollision(self,direction):
        #left or right

        #A little buggy- fix if we have time
        if direction == 'horizontal':
            if self.rect.left <= 0:
                self.rect.left = 0
                self.direction.x *= -1

            if self.rect.right >= 800:
                self.rect.right = 800
                self.direction.x *= -1

        if direction == 'vertical':
            if self.rect.top <= 0:
                self.rect.top = 0
                self.direction.y *= -1

            if self.rect.bottom >= 600:
                self.rect.bottom = 600
                self.direction.y *= -1

    def update(self):
        self.old_rect = self.rect.copy()
        self.input()

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed
        self.rect.x = round(self.pos.x)
        self.collisions('horizontal')
        self.bordercollision('horizontal')
        self.pos.y += self.direction.y * self.speed
        self.rect.y = round(self.pos.y)
        self.collisions('vertical')
        self.bordercollision('vertical')

class PlayerBullet:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = 12
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed


    def update(self, screen):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, position):
         self.image = pygame.image.load('./graphics/bee.png').convert_alpha()
         self.image = pygame.transform.rotozoom(self.image, 0, 1.1)
         self.rect = self.image.get_rect()
         self.rect.center = position
         self.direction = pygame.math.Vector2()
         self.vel = pygame.math.Vector2()
         self.speed = (random.random() * 2) + 1
        
         self.position = pygame.math.Vector2(position)

    def render(self, surface):
        surface.blit(self.image, self.position)

    def chase(self):
       player_vector = pygame.math.Vector2(player.pos)
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


pygame.init()

#general setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#group setup
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

#sprite setup
StaticObstacle((150,300),(100,20),[all_sprites,collision_sprites],'green')
StaticObstacle((250,120),(20,200),[all_sprites,collision_sprites],'yellow')

StaticObstacle((150,450),(200,20),[all_sprites,collision_sprites],'yellow')
StaticObstacle((550,100),(100,20),[all_sprites,collision_sprites],'green')
StaticObstacle((550,400),(20,200),[all_sprites,collision_sprites],'yellow')

StaticObstacle((0,0),(800,20),[all_sprites,collision_sprites],'blue')
StaticObstacle((0,580),(800,20),[all_sprites,collision_sprites],'blue')
StaticObstacle((0,20),(20,780),[all_sprites,collision_sprites],'blue')
StaticObstacle((780,20),(20,780),[all_sprites,collision_sprites],'blue')


player = Player(all_sprites,collision_sprites, 200, 200)
#ball = Ball(all_sprites,collision_sprites)
player_bullets = []


enemies = []

s_width, s_height = screen.get_size()

enemy_spawnpoints = [(50, 50), (s_width - 50, 50), (50, s_height - 50), (s_width - 50, s_height - 50)]

enemy_clock = 0
enemy_wait_time = random.randint(1, 7)

bullet_clock = 15

#loop
while True:

    enemy_clock += 1
    bullet_clock += 1

    if enemy_clock >= enemy_wait_time * 60:
        enemy_clock = 0
        enemy_wait_time = random.randint(1, 4)
        start_pos = random.randint(0, 3)
        enemy = Enemy(enemy_spawnpoints[start_pos])
        enemies.append(enemy)

    #delta time

    mouse_x, mouse_y = pygame.mouse.get_pos()
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and bullet_clock >= 15:
                bullet_clock = 0
                new_bullet = PlayerBullet(player.rect.centerx, player.rect.centery, mouse_x, mouse_y)
                player_bullets.append(new_bullet)  # Add the bullet to the sprite group

    for bullet in player_bullets:
        #bullet position: bullet.x, bullet.y
        #enemy position:  enemy.rect.centerx, enemy.rect.centery
        for enemy in enemies:
            if (bullet.x >= enemy.rect.centerx - 25 and bullet.x <= enemy.rect.centerx + 25):
                if (bullet.y >= enemy.rect.centery - 10 and bullet.y <= enemy.rect.centery + 40):
                    enemies.remove(enemy)
                    player_bullets.remove(bullet)
                    print("Enemy destroyed")

    for enemy in enemies:
        if (player.pos.x >= enemy.rect.centerx - 25 and player.pos.x <= enemy.rect.centerx + 25):
                if (player.pos.y >= enemy.rect.centery - 25 and player.pos.y <= enemy.rect.centery + 25):
                    pygame.quit()
                    sys.exit()





# drawing and updating the screen

    # for sprite in all_sprites.sprites():
    #     pygame.draw.rect(screen,'orange',sprite.old_rect)

    #drawing and updating the screen

    background = pygame.image.load('./graphics/background.jpg') #for bg

    screen.fill('black')
    screen.blit(background, (0, 0))
    all_sprites.update()
    all_sprites.draw(screen)

    for i in range(0,len(enemies)):
      enemies[i].update()
      enemies[i].render(screen)

    # Draw and update bullets

    for bullet in player_bullets:
        bullet.update(screen)
        pygame.draw.circle(screen, (255, 255, 255), (int(bullet.x), int(bullet.y)), 5)

    clock.tick(60)
    pygame.display.update()  

pygame.quit()