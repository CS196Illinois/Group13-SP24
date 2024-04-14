import pygame
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision")


obstacles = []
for _ in range(16):
  obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
  obstacles.append(obstacle_rect)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


run = True
while run:

    screen.fill(BG)

    pos = pygame.mouse.get_pos()

    col = GREEN

    for obstacle in obstacles:
      if obstacle.collidepoint(pos):
        pygame.draw.rect(screen, RED, obstacle)
      else:
         pygame.draw.rect(screen, GREEN, obstacle)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    pygame.display.flip()

pygame.quit()     