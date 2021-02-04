import pygame
from pygame.transform import rotate
from pygame.sprite import Sprite, Group
from pygame.math import Vector2

SIZE = (320, 240)
WHITE = (255, 255, 255)


class Ant(Sprite):

    def __init__(self, size=(25, 25), speed=(2, 2)):
        # Call the parent class (Sprite) constructor
        super(Ant, self).__init__()

        # Load an image of the ant
        self.image = pygame.image.load("ant_worker.png")
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(*size)
        self.rect.update(0, 0, *self.rect.size)
        self.vector = Vector2(speed)

    @property
    def direction(self):
        return self.vector.normalize()

    def update(self):
        self.rect.move_ip(self.vector)

        if self.rect.left < 0 or self.rect.right > SIZE[0]:
            self.vector = self.vector.reflect((1, 0))

        if self.rect.top < 0 or self.rect.bottom > SIZE[1]:
            self.vector = self.vector.reflect((0, 1))

    def draw(self, surface):
        angle = self.vector.angle_to(Vector2(0, -1))
        surface.blit(rotate(self.image, angle), self.rect)


if __name__ == '__main__':

    # Creates a graphical window, based on system hardware
    # settings
    screen = pygame.display.set_mode(SIZE)

    ant = Ant()

    colony = Group(ant)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        colony.update()

        screen.fill(WHITE)

        for ant in colony.sprites():
            ant.draw(screen)

        pygame.display.flip()
