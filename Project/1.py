import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, image_path):
        super().__init__()
        self.position = (x, y)
        self.vel_x = velocity_x
        self.vel_y = velocity_y
        self.image = pygame.image.load("./img/blobLeft.png")
    
    def update(self):
        self.position = (self.position[0] + self.vel_x, self.position[1] + self.vel_y)
    
    def draw(self, surface):
        surface.blit(self.image, self.position)

    def move_left(self):
        velocity_x = -1
    
    def move_right(self):
        velocity_x = 1

    def move_up(self):
        velocity_y = 1

    def move_down(self):
        velocity_y = -1    
    # def stop(self):
    #     for event in pygame.event.get():
    



    


# Initialize Pygame
pygame.init()

# Set the window size
window_size = (1000, 800)

# Create a windowsu
window = pygame.display.set_mode(window_size)

# Create a player sprite
player = Player(320, 240, 0, 0, 'blobLeft.png')

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            system.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_DOWN:
                player.move_down()
            elif event.key == pygame.K_UP:
                player.move_up()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move_right()
            elif event.key == pygame.K_RIGHT:
                player.move_left()
            elif event.key == pygame.K_DOWN:
                player.move_up()
            elif event.key == pygame.K_UP:
                player.move_down()
    
    # Update the player sprite
    player.update()
    
    # Clear the window
    window.fill((255, 255, 255))
    
    # Draw the player sprite
    player.draw(window)
    
    # Update the display
    pygame.display.update()