import pygame

def Init_Display(caption = "Pygame Gravity Simulator"):
    
    from os import environ

    environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

    pygame.init()

    SCREEN_SIZE: tuple = (pygame.display.Info().current_w, pygame.display.Info().current_h)

    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(caption)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    return True