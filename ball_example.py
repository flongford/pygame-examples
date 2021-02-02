import pygame


# NOTE: this appears in many code examples but actually just
#  performs a load of module imports so is optional
# pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = (0, 0, 0)


if __name__ == '__main__':

    # Creates a graphical window, based on system hardware
    # settings
    screen = pygame.display.set_mode(size)

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

        screen.fill(black)
        screen.blit(ball, ball_rect)
        pygame.display.flip()
