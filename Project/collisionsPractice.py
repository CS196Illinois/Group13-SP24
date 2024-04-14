import pygame as p
import random as r

p.init()

screenWidth = 600
screenHeight = 400

screen = p.display.set_mode((screenWidth, screenHeight))
p.display.set_caption("Collision")

rect1 = p.Rect(0, 0, 25, 25)

obstacles = []
for _ in range(16):
    rect2 = p.Rect(r.randint(0, 500), r.randint(0, 300), 25, 25)
    obstacles.append(rect2)

BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

run = True

while run:
    screen. fill(BG)
    col = GREEN

    if rect1.collidelist(obstacles) >= 0:
        col = RED

    pos = p.mouse.get_pos()
    rect1.center = pos

    p.draw.rect(screen, col, rect1)
    for obstacle in obstacles:
        p.draw.rect(screen, BLUE, obstacle)

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
    
    p.display.flip()

p.quit()

