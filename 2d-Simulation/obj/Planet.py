import pygame
from utils.vector2 import *
from random import randint

pygame.init()

class Planet():
    def __init__(self, Xpos: int | float, Ypos: int | float,Radius: int|float, Mass: int|float, Velocity = vector2(0, 0), Width: int|float = 0):
        
        self.pos: 'vector2' = vector2(Xpos, Ypos)
        self.velocity: 'vector2' = Velocity
        self.accleration: 'vector2' = vector2(0, 0)
        self.netforce: 'vector2' = vector2(0, 0)

        self.RADIUS: int|float = Radius
        self.MASS: int|float = Mass
        self.WIDTH: int|float = Width

        self.COLOUR = (randint(100,255), randint(100,255), randint(100,255))

    def UpdateValues(self):
        self.pos =+ self.velocity
        self.velocity += self.accleration
        self.accleration += self.netforce

    def Collision_Check(self, obj: 'Planet'):
        dx = self.pos.X - obj.pos.X
        dy = self.pos.Y - obj.pos.Y
        distance = ((dx ** 2) + (dy ** 2)) ** 0.5

        if distance <= self.RADIUS + obj.RADIUS: return True
        else: return False

    def Update(self):
        self.pos += self.velocity
        self.velocity += self.accleration
        self.accleration += self.netforce

    def Pull(self, obj: "Planet"):
        pass
