import pygame

pygame.init()

def draw(Screen, Planet):
    pygame.draw.circle(Screen, Planet.COLOUR, Planet.pos, Planet.RADIUS)