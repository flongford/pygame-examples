import pygame


# NOTE: this appears in many code examples but actually just
#  performs a load of module imports so is optional in many
#  situations
pygame.init()

SIZE = width, height = (320, 240)
BLACK = (0, 0, 0)


if __name__ == '__main__':

    # Creates a graphical window, based on system hardware
    # settings
    screen = pygame.display.set_mode(SIZE)

    speed = [2, 2]

    ball = pygame.image.load("intro_ball.gif")

    ball_rect = ball.get_rect()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball_rect = ball_rect.move(speed)

        if ball_rect.left < 0 or ball_rect.right > width:
            speed[0] = -speed[0]

        if ball_rect.top < 0 or ball_rect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(BLACK)
        screen.blit(ball, ball_rect)
        pygame.display.flip()
