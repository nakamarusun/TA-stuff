import pygame
import pygame.event
import pygame.display
import object_manager
import pygame.time

import util

from time import time

pygame.display.set_caption("Starfield")

# Inits the pygame library
pygame.init()

while 1:
    # Records the first delta
    begin_time = time()

    # Loads the events to a local var
    util.events = pygame.event.get()

    for ev in util.events:
        # Detects for quitting
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Detects for resizing the window
        elif ev.type == pygame.VIDEORESIZE:
            # Sets the new resolution
            util.resolution = (ev.w, ev.h)
            util.mainSurface = pygame.display.set_mode(util.resolution, pygame.RESIZABLE)

    # Clears the surface buffer
    util.mainSurface.fill( (0, 0, 0) )

    # Updates all the objects
    object_manager.update_objects()

    # Draws fps
    util.draw_fps()

    # Updates display buffer
    pygame.display.flip()

    # Updates delta variable
    util.delta = (time() - begin_time) * 1000

    # Wait for milliseconds to FPS lock
    pygame.time.delay(round((1/util.fps_lock * 1000) - util.delta))