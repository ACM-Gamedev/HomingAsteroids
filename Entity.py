
from pygame import draw
from Vector2 import Vector2
from Circle import Circle
import random
import math


# This class describes game objects in our game
class Entity(object):

    def __init__(self):

        # R G B
        # default color is white
        self.color = (255, 255, 255)

        self.graphicsBounds = Circle(Vector2(0.0, 0.0), 1)

        self.collider = Circle(Vector2(0.0, 0.0), 1)

        self.position = Vector2(0.0, 0.0)
        self.velocity = Vector2(0.0, 0.0)

        self.acceleration = Vector2(0.0, 0.0)

    def update(self, dt):

        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

        # Update graphical and physical bounds
        self.graphicsBounds.center = self.position
        self.collider.center = self.position

    def render(self, screen):

        center = self.graphicsBounds.center
        radius = self.graphicsBounds.radius

        # Pygame needs a 2-tuple of integers as the center of a circle
        center_int = (int(center.x), int(center.y))

        draw.circle(screen, self.color, center_int, radius)
