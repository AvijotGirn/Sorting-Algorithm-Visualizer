import math

import pygame
import random
pygame.init()


class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = 155,171,184

    COLORS = [
        (238,227,203),
        (215,192,174),
        (150,126,118)
    ]

    FONT = pygame.font.SysFont('Arial',30)
    LARGE_FONT = pygame.font.SysFont('Arial', 40)
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

    def draw(self, algo_name, ascending):
        self.window.fill(self.BACKGROUND_COLOR)

        title = self.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,self.BLACK)
        self.window.blit(title, (self.width / 2 - title.get_width() / 2, 5))

        controls = self.FONT.render("R - Reset | SPACE - Starting Sorting | A - Ascending | D - Descending", 1, self.BLACK)
        self.window.blit(controls, (self.width/2 - controls.get_width()/2,45))

        sorting = self.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, self.BLACK)
        self.window.blit(sorting,(self.width/2 - sorting.get_width()/2, 75))

        draw_list(self)
        pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_background=False):
    lst = draw_info.lst

    if clear_background:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.COLORS[i % 3]  # Cycle through COLORS[0], COLORS[1], and COLORS[2]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.block_height * val))

    if clear_background:
        pygame.display.update()


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j:draw_info.RED, j+1:draw_info.BLACK}, True)
                yield True    # Pauses the execution half way and picks up where it left off
                              # To account for user being able to use controls while this is running

    return lst


def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1,len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i-1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i-1]
            i = i-1
            lst[i] = current
            draw_list(draw_info, {i-1:draw_info.RED, i:draw_info.BLACK}, True)
            yield True
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    # Testing
    n = 50
    min_val = 0
    max_val = 100
    lst = generate_starting_list(n,min_val,max_val)
    draw_info = DrawInformation(1000,800, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algo_generator = None
    ###################################################

    while run:
        clock.tick(30)  #FPS. i.e. max number of times this loop runs per second
        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw_info.draw(sorting_algo_name, ascending)

        pygame.display.update()  # Draw window and show on screen -> updates display

        for event in pygame.event.get():  #returns list of all events that have occurred since the last loop
            if event.type == pygame.QUIT:  # Handle X Button
                run = False

            if event.type != pygame.KEYDOWN:   # If no key pressed
                continue

            if event.key == pygame.K_r:       # Implement reset key, if 'R' is pressed, reset list (new list)
                lst = generate_starting_list(n,min_val,max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algo_generator = sorting_algorithm(draw_info, ascending)  # Need to have this because of yield
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
