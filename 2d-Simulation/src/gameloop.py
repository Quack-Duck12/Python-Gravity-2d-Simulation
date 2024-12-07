import pygame
from os import environ
from src.Events import *

def game_loop():

    environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

    pygame.init()

    DISPLAY_SIZE: tuple = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    SCREEN_SIZE: tuple = (int(DISPLAY_SIZE[0] / 4), int(DISPLAY_SIZE[1] / 4))

    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)

    pygame.display.set_caption("Python 2d gravity simulation")

    FPS: int = 60
    FPSCLOCK = pygame.time.Clock()

    Running: bool = True

    while Running:

        deltatime = FPSCLOCK.tick(FPS)

        Running = handle_events(pygame.event.get())

        Scaled_Surface = pygame.transform.scale(SCREEN, SCREEN_SIZE)
        DISPLAY.blit(Scaled_Surface, (0,0))

        pygame.display.flip()

        if not Running: pygame.quit()