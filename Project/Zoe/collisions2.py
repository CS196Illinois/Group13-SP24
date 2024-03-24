import pygame, sys, time

#defining classes
class StaticObstacle(pygame.sprite.Sprite):
    def __init__(self,pos,size,groups):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

class Player(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        #image
        self.image = pygame.Surface((30,60))
        self.image.fill('blue')

        #position
        self.rect = self.image.get_rect(topleft = (640,360))
        self.old_rect = self.rect.copy()

        #movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()

        #movement input
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = -1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        

        def update(self,dt):
            self.old_rect = self.rect.copy()
            self.input()

            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()

            self.pos += self.direction * self.speed * dt
            self.rect.topleft = round(self.pos.x), round(self.pos.y)

class Ball(pygame.sprite.Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image = pygame.Surface((40,40))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = (640,360))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(1,1)
        self.speed = 400
        self.old_rect = self.rect.copy()

#general setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#group setup
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

#sprite setup
StaticObstacle((100,300),(100,50),[all_sprites,collision_sprites])
StaticObstacle((800,600),(100,200),[all_sprites,collision_sprites])
StaticObstacle((900,200),(200,10),[all_sprites,collision_sprites])
Player(all_sprites)
Ball(all_sprites)

#loop
last_time = time.time()
while True:

    #delta time
    dt = time.time() - last_time
    last_time = time.time()

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #drawing and updating the screen
    screen.fill('black')
    all_sprites.update(dt)

    all_sprites.draw(screen)

    pygame.display.update() 

pygame.quit()