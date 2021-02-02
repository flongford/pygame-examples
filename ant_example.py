import pygame
from pygame.sprite import Sprite

SIZE = (320, 240)
WHITE = (255, 255, 255)


class Ant(Sprite):

    def __init__(self, size=(25, 25), speed=(2, 2)):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load an image of the ant
        self.surface = pygame.image.load("ant_worker.png")
        self.rect = self.surface.get_rect()
        self.rect.inflate(*size)

        self.speed = list(speed)

    def update(self):
        ant.rect.move_ip(self.speed)

        if ant.rect.left < 0 or ant.rect.right > SIZE[0]:
            self.speed[0] = -self.speed[0]

        if ant.rect.top < 0 or ant.rect.bottom > SIZE[1]:
            self.speed[1] = -self.speed[1]

    def draw(self, surface):
        surface.blit(self.surface, self.rect)


if __name__ == '__main__':

    # Creates a graphical window, based on system hardware
    # settings
    screen = pygame.display.set_mode(SIZE)

    ant = Ant()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ant.update()

        screen.fill(WHITE)
        ant.draw(screen)
        pygame.display.flip()
