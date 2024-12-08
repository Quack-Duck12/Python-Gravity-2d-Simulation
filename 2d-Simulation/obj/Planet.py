from math import dist
import pygame
from utils.vector2 import *
from random import randint

pygame.init()

class Planet():
    def __init__(self, Xpos: int | float, Ypos: int | float,Radius: int|float, Mass: int|float, Velocity = vector2(0, 0), Width: int|float = 0):
        
        self.pos: 'vector2' = vector2(Xpos, Ypos)
        self.velocity: 'vector2' = Velocity
        self.accleration: 'vector2' = vector2(0, 0)

        self.RADIUS: int|float = Radius
        self.MASS: int|float = Mass
        self.WIDTH: int|float = Width

        self.COLOUR = (randint(100,255), randint(100,255), randint(100,255))

    def Collision_Check(self, obj: 'Planet'):
        dx = self.pos.X - obj.pos.X
        dy = self.pos.Y - obj.pos.Y
        distance = ((dx ** 2) + (dy ** 2)) ** 0.5

        if distance <= self.RADIUS + obj.RADIUS: return True
        else: return False

    def UpdateValues(self, deltatime):
        self.pos += self.velocity * deltatime + 0.5 * self.accleration * deltatime**2
        self.velocity += self.accleration * deltatime


    def Pull(self, obj: "Planet", Grav_Const: int|float = 1):

        barycenter = ((self.MASS * self.pos) + (obj.MASS * obj.pos)) / (self.MASS + obj.MASS)
        #print(type(barycenter))
        distance = (((self.pos.X - barycenter.X)**2) + ((self.pos.Y - barycenter.Y)**2))**0.5

        force_magnitude = Grav_Const * self.MASS * obj.MASS / distance**2
        force_direction = (obj.pos - self.pos) / distance
        force = force_magnitude * force_direction

        self.Force = force
        obj.Force = -1 * force

        # Update the accelerations of both objects
        self.accleration += self.Force / self.MASS
        obj.accleration += obj.Force / obj.MASS

