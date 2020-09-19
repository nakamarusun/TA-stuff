import pygame
import pygame.display
from time import time

events = None
resolution = (800, 600)
mainSurface = pygame.display.set_mode(resolution, pygame.RESIZABLE)

def get_middle_res():
    return [resolution[0]/2, resolution[1]/2]

def get_milli() -> int:
    return int(round(time() * 1000))