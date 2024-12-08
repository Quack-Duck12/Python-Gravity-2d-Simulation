import pygame

from sys import path as pth
from os import path

pth.append(path.abspath(path.join(path.dirname(__file__), '..')))

from obj.Planet import Planet

pygame.init()

def draw(Screen, object: "Planet"):
    pygame.draw.circle(Screen, object.COLOUR, object.pos.Value(), object.RADIUS, object.WIDTH)