import pygame
from sys import path as pth
from os import path

pth.append(path.abspath(path.join(path.dirname(__file__), '..')))

from utils.draw import draw
from gamecode import InitValues

def gameloop():

    Screen = InitValues.Screens()
    Obj_list = list()

    Running: bool = True

    while Running:

        Screen.fill("Black")

        Running, Obj_list = InitValues.handle_events(pygame.event.get(), Obj_list)

        if not Running:
            pygame.quit()
            from sys import exit
            exit()

        for Obj in Obj_list:
            Obj.Update()
            draw(Screen, Obj)

        pygame.display.flip()


gameloop()