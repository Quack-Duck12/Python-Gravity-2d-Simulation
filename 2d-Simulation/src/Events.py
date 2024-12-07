import pygame

def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
    return True