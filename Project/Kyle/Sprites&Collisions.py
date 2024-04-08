import pygame

window_size = (1500, 700)
window = pygame.display.set_mode((window_size[0], window_size[1]))
pygame.display.set_caption('Sprites & Characters')
window.fill((0, 0, 0))
pygame.display.update()
white = (255, 255, 255)
# blob variables for movement and creation

blob_dir_x = 0
blob_dir_y = 0
blob_width = 50
blob_height = 50
blob_x = 750
blob_y = 350
blob_speed = 3

def update_blob_position():
    global blob_x
    global blob_y
    global blob_dir_x
    global blob_dir_y
    if blob_dir_x > 0:
        if blob_dir_x < 1500 - blob_width:
            blob_x += blob_dir_x * blob_speed
    if blob_dir_x < 0:
        if blob_x > 0:
            blob_x += blob_dir_x * blob_speed
    if blob_dir_y > 0:
        if blob_dir_y < 1200 - blob_height:
            blob_y += blob_dir_y * blob_speed
    if blob_dir_y < 0:
        if blob_y > 0:
            blob_y += blob_dir_y * blob_speed

run = True
while run:

    update_blob_position()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                blob_dir_x = -1
            if event.type == pygame.K_RIGHT:
                blob_dir_x = 1
            if event.type == pygame.K_UP:
                blob_dir_y = 1
            if event.type == pygame.K_DOWN:
                blob_dir_y = -1
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT:
                blob_dir_x = 0
            if event.type == pygame.K_RIGHT:
                blob_dir_x = 0
            if event.type == pygame.K_UP:
                blob_dir_y = 0
            if event.type == pygame.K_DOWN:
                blob_dir_y = 0

    blob = pygame.draw.rect(window, (white), [blob_x, blob_y, blob_width / 2, blob_height / 2])
    image = pygame.image.load('./img/blobLeft.png').convert()
    # blob_rect = image.get_rect()
    window.blit(image, blob)
    pygame.display.update()

pygame.display.update()