import pygame, sys, time

#for ball: bottom of sprite and left of sprite collisions arent working its teleporting

#defining classes
class StaticObstacle(pygame.sprite.Sprite):
    def __init__(self,pos,size,groups,color):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,obstacles):
        super().__init__(groups)
        #image
        self.image = pygame.Surface((30,60))
        self.image.fill('blue')
        self.obstacles = obstacles

        #position
        self.rect = self.image.get_rect(topleft = (200,200))
        self.old_rect = self.rect.copy()

        #movement
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 200

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
        if direction == 'horizontal':
            if self.rect.left <= 0:
                self.rect.left = 0
                self.direction.x *= -1

            if self.rect.right >= 600:
                self.rect.right = 600
                self.direction.x *= -1

        if direction == 'vertical':
            if self.rect.top <= 0:
                self.rect.top = 0
                self.direction.y *= -1

            if self.rect.bottom >= 400:
                self.rect.bottom = 400
                self.direction.y *= -1

    def update(self,dt):
        self.old_rect = self.rect.copy()
        self.input()

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collisions('horizontal')
        self.bordercollision('horizontal')
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collisions('vertical')
        self.bordercollision('vertical')

#make power up class extending ball class

class Ball(pygame.sprite.Sprite):
    def __init__(self,groups,obstacles):
        super().__init__(groups)
        self.image = pygame.Surface((20,20))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = (10,10))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(1,1)
        self.speed = 200
        self.old_rect = self.rect.copy()
        self.obstacles = obstacles

    def collisions(self,direction):
        self.obstacles = pygame.sprite.spritecollide(self,collision_sprites,False)

        if pygame.sprite.collide_rect(player,self):
            self.obstacles.append(player)

        for sprite in self.obstacles:
            if direction == 'horizontal':
                #ball moving right, colliding w sprite's left
                if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.rect.left:

                    self.rect.right = sprite.rect.left
                    self.pos.x = self.rect.x
                    self.direction.x *= -1
                    self.pos.x -= 1

                #ball moving left, colliding w sprite's right
                if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.rect.right:
                    self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.x
                    self.direction.x *= -1
                    self.pos.x += 1

            if direction == 'vertical':
                #ball moving down, colliding w sprite top
                if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.rect.top:
                    self.rect.bottom = sprite.rect.top
                    self.pos.y = self.rect.y
                    self.direction.y *= -1
                    self.pos.y -= 1

                #ball moving up, colliding w sprite top
                if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.rect.bottom:
                    self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.direction.y *= -1
                    self.pos.y += 1

    def bordercollision(self,direction):
        #colliding w left or right side of window
        if direction == 'vertical':
            #bottom
            if self.rect.bottom >= 400:
                self.rect.bottom = 400
                self.pos.y = self.rect.y
                self.direction.y *= -1
                self.pos.y -= 1

            #top
            if self.rect.top <= 0:
                self.rect.top = 0
                self.pos.y = self.rect.y
                self.direction.y *= -1
                self.pos.y += 1

        if direction == 'horizontal':
            #left
            if self.rect.left <= 0:
                self.rect.left = 0
                self.pos.x = self.rect.x
                self.direction.x *= -1
                self.pos.x += 1

            #right
            if self.rect.right >= 600:
                self.rect.right = 600
                self.pos.x = self.rect.x
                self.direction.x *= -1
                self.pos.x -= 1


    def update(self,dt):
        self.old_rect = self.rect.copy()
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collisions('horizontal')
        self.bordercollision('horizontal')
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collisions('vertical')
        self.bordercollision('vertical')

pygame.init()

#general setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#group setup
all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

#sprite setup
StaticObstacle((0,0),(150,20),[all_sprites,collision_sprites],'yellow')
StaticObstacle((150,0),(20,300),[all_sprites,collision_sprites],'blue')
StaticObstacle((150,300),(100,20),[all_sprites,collision_sprites],'green')
StaticObstacle((250,120),(20,200),[all_sprites,collision_sprites],'yellow')
player = Player(all_sprites,collision_sprites)
ball = Ball(all_sprites,collision_sprites)

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

    for sprite in all_sprites.sprites():
        pygame.draw.rect(screen,'orange',sprite.old_rect)

    #drawing and updating the screen
    screen.fill('black')
    all_sprites.update(dt)
    all_sprites.draw(screen)

    pygame.display.update() 

pygame.quit()