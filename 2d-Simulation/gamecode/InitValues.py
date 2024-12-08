import pygame
from random import randint  #Remove Later

from sys import path as pth
from os import path
pth.append(path.abspath(path.join(path.dirname(__file__), '..')))

from obj.Planet import Planet
from utils.vector2 import vector2

pygame.init()

def Screens():

    Info = pygame.display.Info()
    SCREEN_SIZE: tuple = (Info.current_w - 50, Info.current_h - 50)
    del Info

    Real_Screen = pygame.display.set_mode(SCREEN_SIZE, vsync=True, flags=pygame.RESIZABLE)

    return(Real_Screen)

def handle_events(events: 'pygame.event.Event', Obj_List: list):
    for event in events:
        if event.type == pygame.QUIT:
            return [False, None]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            NewPlanet = Planet(
                mousepos[0],
                mousepos[1],
                10,#randint(5,20),
                0.1,
                vector2(0,0)#vector2((randint(-10,10)),randint(-10,10))
                )
            Obj_List.append(NewPlanet)
            
    return [True, Obj_List]