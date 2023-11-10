import math

import pygame
import random
pygame.init()


class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = WHITE

    GREYS = [
        (128,128,128),
        (160,160,160),
        (192,192,192)
    ]

    SIDE_PAD = 100  # pixels
    TOP_PAD = 150

    def __init__(self,w,h,lst):
        self.width = w
        self.height = h

        self.window = pygame.display.set_mode((w,h))   # Setting the pygame window size
        pygame.display.set_caption("Sorting Algorithm Visualizer")   # Window name
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))      # Dynamic way to set the area in which the bars
                                                                                # show, subtract SIDEBAR to cut off the sides,
                                                                                # then divide by num of elements
        self.block_height = int((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

    def draw(self):
        self.window.fill(self.BACKGROUND_COLOR)
        draw_list(self)
        pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GREYS[i % 3]  # Cycle through GREYS[0], GREYS[1], and GREYS[2]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.block_height * val))


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    # Testing
    n = 50
    min_val = 0
    max_val = 100
    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(800,600, lst)
    ###################################################

    while run:
        clock.tick(60)  #FPS. i.e. max number of times this loop runs per second
        draw_info.draw()

        pygame.display.update()  # Draw window and show on screen -> updates display

        for event in pygame.event.get():  #returns list of all events that have occurred since the last loop
            if event.type == pygame.QUIT:  # Handle X Button
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
