import pygame
import random
pygame.init()


class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    GREY = 128,128,128
    BACKGROUND_COLOR = WHITE

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
        self.min_value = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))      # Dynamic way to set the area in which the bars
                                                                                # show, subtract SIDEBAR to cut off the sides,
                                                                                # then divide by num of elements
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_value))
        self.start_x = self.SIDE_PAD // 2


def generate_starting_list(n, min_val, max_val):
    lst =[]
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

        pygame.display.update()  # Draw window and show on screen -> updates display

        for event in pygame.event.get():  #returns list of all events that have occurred since the last loop
            if event.type == pygame.QUIT:  # Handle X Button
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()
