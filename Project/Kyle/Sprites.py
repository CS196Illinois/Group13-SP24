import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprites & Collisions")

WHITE = (255, 255, 255)
WINDOW.fill(WHITE)
pygame.display.update()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, vel_x, vel_y, image_path):
        super().__init__()
        self.position = (x, y)
        self.velocity = (vel_x, vel_y)
        self.image = pygame.image.load('./img/blobLeft.png')

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def move_right(self):
        self.velocity = (1, self.velocity[1])

    def move_left(self):
        self.velocity = (-1, self.velocity[1])

    def move_up(self):
        self.velocity = (self.velocity[0], 1)

    def move_down(self):
        self.velocity = (self.velocity[0], -1)

        


def main():

    run = True

    player = Player(500, 400, 0, 0, 'blobLeft.png')
    while run:

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_DOWN:
                    player.move_down()
                if event.type == pygame.K_UP:
                    player.move_up()
                if event.type == pygame.K_LEFT:
                    player.move_left()
                if event.type == pygame.K_RIGHT:
                    player.move_right()

            if event.type == pygame.QUIT:
                run = False


        player.update()
        player.draw(WINDOW)
        pygame.display.update()


if __name__ == "__main__":
    main()
