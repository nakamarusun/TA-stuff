from pygame import event
import pygame
import util
from math import ceil, floor
import random
import pygame.draw
import pygame.gfxdraw

class Star_Manager:

    max_size = 5
    max_speed = 0.035
    min_speed = 0.005

    def __init__(self):
        super().__init__()

        # Star list
        self.star_list = [] # This is list inside of list, [[x, y, speed, size], ...]
        self.star_timer = 0

    def step(self):

        mid = util.get_middle_res()

        # Simple timer functionality
        if (self.star_timer < util.get_milli()):
            # Coords
            coords = [random.randint(-util.resolution[0]//2, util.resolution[0]//2), random.randint(-util.resolution[1]//2, util.resolution[1]//2)]
            # Append a new star in the array
            self.star_list.append([
                *coords,
                1 + Star_Manager.min_speed + (random.random() * Star_Manager.max_speed),
                abs(coords[0]/mid[0]) + abs(coords[1]/mid[1]) * 5
            ])
            # Restart timer
            self.star_timer = util.get_milli() + random.randint(1, 2)

        counter = 0 # Counter to count how many items has been iterated.
        pop_list = [] # List of objects that need to be deleted from the list.

        # Draws all of the star in the list
        for star in self.star_list:
            # Updates the star function
            star[0] *= star[2]
            star[1] *= star[2]
            star[3] += 0.005

            # Draws the stars appended with half of resolution
            # Not anti-aliased
            rect = [ int(i + j) for i, j in zip([star[0], star[1]], util.get_middle_res()) ]
            pygame.draw.rect(util.mainSurface, (255, 255, 255), [rect, [ceil(star[3]), ceil(star[3])]] )

            # If object is out of the screen, delete it.
            if (abs(star[0]) > mid[0] or abs(star[1]) > mid[1]):
                pop_list.append(counter - len(pop_list))

            counter += 1

        # Remove everything in the pop list
        for i in pop_list:
            self.star_list.pop(i)

        # Detects keypress in keyboard to increase speed.
        for ev in util.events:
            if (ev.type == pygame.KEYDOWN):
                if (ev.key == pygame.K_UP):
                    Star_Manager.max_speed += 0.001
                if (ev.key == pygame.K_DOWN):
                    Star_Manager.max_speed -= 0.001
