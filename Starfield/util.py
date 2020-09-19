import pygame
import pygame.display
import pygame.font
from time import time

pygame.font.init()

events = None
resolution = (800, 600)
mainSurface = pygame.display.set_mode(resolution, pygame.RESIZABLE)
fps_lock = 60
delta = 0 # Time passed since beginning of frame in milliseconds
def_font = pygame.font.Font(pygame.font.get_default_font(), 12)

def get_middle_res():
    return [resolution[0]/2, resolution[1]/2]

def get_milli() -> int:
    return int(round(time() * 1000))

def draw_fps():
    fps = str(round(1/(delta/1000))) if delta != 0 else ">1000"
    mainSurface.blit(def_font.render(fps, False, (255, 255, 255)), (5, 5))