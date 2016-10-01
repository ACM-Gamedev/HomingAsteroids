
from pygame import Rect, draw
from Vector2 import Vector2

# This class describes game objects in our game

class Entity:

    def __init__(self):

        # R G B
        # default color is white
        self.color = (255, 255, 255)

        self.graphicsBounds = Rect(0, 0, 1, 1)

        self.collider = Rect(0, 0, 1, 1)

        self.position = Vector2(0, 0)
        self.velocity = Vector2(0, 0)

        self.acceleration = Vector2(0, 0)

    def update(self, dt):

        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt


        gw = self.graphicsBounds.width
        gh = self.graphicsBounds.height
        self.graphicsBounds.topleft = (self.position.x - gw/2, self.position.y - gh/2)

        cw = self.collider.width
        ch = self.collider.height
        self.collider.topleft = (self.position.x - cw/2, self.position.y - ch/2)

    def render(self, screen):

        draw.rect(screen, self.color, self.graphicsBounds)
