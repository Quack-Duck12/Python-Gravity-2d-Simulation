
import pygame
from sys import path as pth
from os import path

pth.append(path.abspath(path.join(path.dirname(__file__), '..')))

from utils.draw import draw
from gamecode import InitValues
from obj.Planet import Planet

def gameloop():

    FPS = 45
    FPSCLOCK = pygame.time.Clock()

    Screen = InitValues.Screens()
    Obj_list: list["Planet"] = list()

    Running: bool = True

    while Running:

        deltatime = FPSCLOCK.tick(FPS)

        Screen.fill("Black")

        Running, Obj_list = InitValues.handle_events(pygame.event.get(), Obj_list)

        if not Running:
            pygame.quit()
            from sys import exit
            exit()

        for index, Obj in enumerate(Obj_list):
            
            for next_index in range(index + 1, len(Obj_list)):
                Obj.Pull(Obj_list[next_index], Grav_Const=5)

            Obj.UpdateValues(deltatime)
            draw(Screen, Obj)

        pygame.display.flip()
