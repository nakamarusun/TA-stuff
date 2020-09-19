import pygame
import pygame.event
import pygame.display
import object_manager

import util

pygame.display.set_caption("Starfield")

# Inits the pygame library
pygame.init()

while 1:
    # Loads the events to a local var
    events = pygame.event.get()

    for ev in events:
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

    # Updates display buffer
    pygame.display.flip()