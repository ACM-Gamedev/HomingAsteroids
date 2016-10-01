import pygame
import sys
from Entity import Entity
from Vector2 import Vector2

pygame.init()

screen_size = (1200, 700)

# Bits per pixel, 8 bits for each RGBA value.
bpp = 32
screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE, bpp)

player = Entity()
player.graphicsBounds.width = 40
player.graphicsBounds.height = 40

# Also set the collider bounds.

player.position.x = 100
player.position.y = 100
player.color = (255, 0, 0)
accel = 200

def take_input(keys):

    xdir = 0.0
    ydir = 0.0

    if keys[pygame.K_a]:
        xdir = -1

    elif keys[pygame.K_d]:
        xdir = 1

    if keys[pygame.K_w]:
        ydir = -1

    elif keys[pygame.K_s]:
        ydir = 1

    direction = Vector2(xdir, ydir)
    direction.normalize()

    player.acceleration = direction * accel

fps = 60
delta_time = 0.0
last_frame_time = 0.0

quit = False
while not quit:

    start_frame_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit = True

    keys = pygame.key.get_pressed()
    take_input(keys)

    player.update(delta_time)

    screen.fill((0,0,0))

    player.render(screen)

    pygame.display.update()

    # Get elapsed time between frames in seconds
    delta_time = (start_frame_time - last_frame_time) / 1000.0

    last_frame_time = start_frame_time
