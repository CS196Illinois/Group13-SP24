import pygame
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision")

rect_1 = pygame.Rect(0, 0, 25, 25)

obstacles = []
for _ in range(16):
  obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
  obstacles.append(obstacle_rect)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.mouse.set_visible(False)

run = True
while run:

    screen.fill(BG)

    col = GREEN

    if rect_1.collidelist(obstacles) >= 0:
      print(rect_1.collidelist(obstacles))
      col = RED

    pos = pygame.mouse.get_pos()
    rect_1.center = pos

    pygame.draw.rect(screen, col, rect_1)
    for obstacle in obstacles:
      pygame.draw.rect(screen, BLUE, obstacle)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    pygame.display.flip()

pygame.quit()     