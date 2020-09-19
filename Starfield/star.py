from util import *
from math import ceil, floor
import random
import pygame.draw
import pygame.gfxdraw

class Star_Manager:
    
    def __init__(self):
        super().__init__()

        # Star list
        self.star_list = []
        self.star_timer = 0

    def step(self):

        # Simple timer functionality
        if (self.star_timer < get_milli()):
            # Do the action
            self.star_list.append(Star())
            # Restart timer
            self.star_timer = get_milli() + random.randint(2, 8)

        
        counter = 0
        pop_list = []
        # Draws all of the star in the list
        for star in self.star_list:
            # Updates the star function
            star.step()

            # Draws the stars appended with half of resolution
            # Not anti-aliased
            if (star.size < 1):
                pygame.gfxdraw.pixel(mainSurface, *[ int(i + j) for i, j in zip(star.coords, get_middle_res()) ], (255, 255, 255))
            else:
                # pygame.draw.circle(mainSurface, (255, 255, 255), [ int(i + j) for i, j in zip(star.coords, get_middle_res()) ], ceil(star.size))
                rect = [ int(i + j) for i, j in zip(star.coords, get_middle_res()) ]
                pygame.draw.rect(mainSurface, (255, 255, 255), [rect, [ceil(star.size), ceil(star.size)]] )

            # Anti-Aliased
            # pygame.gfxdraw.aacircle(mainSurface, *[ int(i + j) for i, j in zip(star.coords, get_middle_res()) ], star.size, (255, 255, 255))
            # pygame.gfxdraw.filled_circle(mainSurface, *[ int(i + j) for i, j in zip(star.coords, get_middle_res()) ], star.size, (255, 255, 255))

            # If object is out of bounds, delete it.
            mid = get_middle_res()
            if (abs(star.coords[0]) > mid[0] or abs(star.coords[1]) > mid[1]):
                pop_list.append(counter - len(pop_list))

            counter += 1

        for i in pop_list:
            self.star_list.pop(i)

class Star:

    def __init__(self):
        super().__init__()

        # Initial Variables
        mid = get_middle_res()
        self.coords = [random.randint(-resolution[0]/2, resolution[0]/2), random.randint(-resolution[1]/2, resolution[1]/2)]
        self.size = abs(self.coords[0]/mid[0]) + abs(self.coords[1]/mid[1]) * 5
        self.speed = random.random() * 0.005
        self.cur_speed = 1.005 + self.speed

    def step(self):
        self.coords = [ i * self.cur_speed for i in self.coords ]
        self.size += 0.005