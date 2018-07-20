"""
title: smiley
author: Zyden Walcher
date: 7/20/18 smiley
"""
"""
 Simple graphics demo
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (249, 249, 11)
ORANGE = (249, 148, 33)

PI = 3.141592653
x_coord, x_speed, y_coord, y_speed = 0, 0, 0, 0
ball_pos_x, ball_pos_y = 310, 310
ball_speed_x, ball_speed_y = 0, 4

# Set the height and width of the screen
size = (600, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Set Up")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


def draw_stick_figure(screen, x, y):
    pygame.draw.circle(screen, YELLOW, [200 + x, 200 + y], 100)
    pygame.draw.ellipse(screen, BLACK, [150 + x, 130 + y, 20, 50])
    pygame.draw.ellipse(screen, BLACK, [225 + x, 130 + y, 20, 50])
    pygame.draw.arc(screen, BLACK, [140 + x, 155 + y, 110, 100], PI, 0, 5)
    pygame.draw.line(screen, BLACK, [200 + x, 300 + y], [200 + x, 430 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 350 + y], [100 + x, 250 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 350 + y], [350 + x, 400 + y], 5)
    pygame.draw.line(screen, BLACK, [200 + x, 430 + y], [50 + x, 500 + y], 5)


def draw_basketball(screen, x, y):
    pygame.draw.circle(screen, ORANGE, [x, y], 50)


# Loop as long as done == False
while not done:
    if ball_pos_y > (550 + y_coord):
        ball_speed_y = -3
    if ball_pos_y < (250 + y_coord):
        ball_speed_y = 3
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                        x_speed = 3
            elif event.key == pygame.K_UP:
                        y_speed = -3
            elif event.key == pygame.K_DOWN:
                        y_speed = 3
        elif event.type == pygame.KEYUP:
            x_speed = 0
            y_speed = 0

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    ball_pos_y += ball_speed_y
    ball_pos_x = x_coord + 65

    draw_stick_figure(screen, x_coord, y_coord)
    draw_basketball(screen, ball_pos_x, ball_pos_y)
# Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)


# Be IDLE friendly
pygame.quit()
