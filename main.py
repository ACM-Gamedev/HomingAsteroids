
import pygame
import sys
from Entity import *
from Vector2 import Vector2
from random import randint, uniform
from pygame import mixer

# Init pygame libraries
mixer.pre_init(22050, -16, 40, 4096 / 4)
pygame.init()
mixer.init()

# Setup pygame window
screen_size = (800, 800)

# Bits per pixel, 8 bits for each RGBA value.
bpp = 32
screen = pygame.display.set_mode(screen_size, pygame.HWSURFACE, bpp)

# Load some sound effects
laser_shot_sfx = mixer.Sound("Assets/laser_shot.wav")
hit_sfx = mixer.Sound("Assets/hit.wav")

# Setup the player entity
player = Entity()
player.graphicsBounds.radius = 10
player.collider.radius = 10

player.position = Vector2(screen_size[0]/2, screen_size[1]/2)
player.color = (255, 0, 0)
player.max_speed = 200
accel = 200


def take_input(keys):

    if player is None:
        return

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


delta_time = 0.0
last_frame_time = 0.0

asteroid_spawn_time = 2.0
asteroid_timer = 0.0

quit = False
while not quit:

    start_frame_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quit = True

    keys = pygame.key.get_pressed()
    take_input(keys)

    if player is not None:
        player.update(delta_time)

    screen.fill((25, 10, 35))

    if player is not None:
        player.render(screen)

    pygame.display.update()

    # Get elapsed time between frames in seconds
    delta_time = (start_frame_time - last_frame_time) / 1000.0

    last_frame_time = start_frame_time
