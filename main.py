import pygame

# initialize
pygame.init()

blue = (0, 0, 255)
white = (255, 255, 255)

display_width = 1000
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Bouncing Ball')

ball_x = 0
ball_y = 0

ball_radius = 15

ball_x_velocity = 1
ball_y_velocity = 1

FPS = 100
clock = pygame.time.Clock()


exit_sim = False

while not exit_sim:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_sim = True

    display.fill(white)
    pygame.draw.circle(display, blue, (int(ball_x), int(ball_y)), ball_radius)
    pygame.display.update()

    ball_y_velocity += 0.1

    if ball_y_velocity > 0:
        ball_y_velocity -= 0.005

    if ball_x + ball_radius > display_width:
        ball_x_velocity = -abs(ball_x_velocity)
    elif ball_x - ball_radius < 0:
        ball_x_velocity = abs(ball_x_velocity)
    elif ball_y + ball_radius > display_height:
        ball_y_velocity = -(ball_y_velocity)
    elif ball_y - ball_radius < 0:
        ball_y_velocity = abs(ball_y_velocity)

    ball_x += ball_x_velocity
    ball_y += ball_y_velocity

    clock.tick(FPS)

pygame.quit()
quit()