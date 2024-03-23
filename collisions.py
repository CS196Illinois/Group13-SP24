import pygame
import random
import sys
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Project")

#making rectangle and obstacles
rect_1 = pygame.Rect(0, 0, 25, 25)
obstacles = []
for _ in range(16):
    obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300,), 25, 25)
    obstacles.append(obstacle_rect)

#colors
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PURPLE = (100, 0, 100)


run = True
while run:
    screen.fill(BLUE)

    col = GREEN
    if rect_1.collidelist(obstacles) >= 0: #doesnt return boolean, -1 if no coll.
        #value returns which number rect it collides with
        col = RED
        pygame.time.delay(1000)
        rect_1 = pygame.Rect(0, 0, 25, 25) #added

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and rect_1.collidelist(obstacles) == -1:
        rect_1.move_ip(-1, 0)
    elif key[pygame.K_d] == True and rect_1.collidelist(obstacles) == -1:
        rect_1.move_ip(1, 0)
    elif key[pygame.K_w] == True and rect_1.collidelist(obstacles) == -1:
        rect_1.move_ip(0, -1)
    elif key[pygame.K_s] == True and rect_1.collidelist(obstacles) == -1:
        rect_1.move_ip(0, 1)

    #draw rectangles
    pygame.draw.rect(screen, col, rect_1)
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
            sys.exit()

    pygame.time.delay(10)

    pygame.display.flip()

pygame.quit()