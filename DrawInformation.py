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


    def draw_list(self, color_positions=None, clear_background=False):
        if color_positions is None:
            color_positions = {}
        lst = self.lst

        if clear_background:
            clear_rect = (self.SIDE_PAD // 2, self.TOP_PAD, self.width - self.SIDE_PAD,
                          self.height - self.TOP_PAD)
            pygame.draw.rect(self.window, self.BACKGROUND_COLOR, clear_rect)

        for i, val in enumerate(lst):
            x = self.start_x + i * self.block_width
            y = self.height - (val - self.min_val) * self.block_height

            color = self.COLORS[i % 3]  # Cycle through COLORS[0], COLORS[1], and COLORS[2]

            if i in color_positions:
                color = color_positions[i]

            pygame.draw.rect(self.window, color, (x, y, self.block_width, self.block_height * val))

        if clear_background:
            pygame.display.update()


    def draw(self, algo_name, ascending):
        self.window.fill(self.BACKGROUND_COLOR)

        title = self.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,self.BLACK)
        self.window.blit(title, (self.width / 2 - title.get_width() / 2, 5))

        controls = self.FONT.render("R - Reset | SPACE - Starting Sorting | A - Ascending | D - Descending", 1, self.BLACK)
        self.window.blit(controls, (self.width/2 - controls.get_width()/2,45))

        sorting = self.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, self.BLACK)
        self.window.blit(sorting,(self.width/2 - sorting.get_width()/2, 75))

        self.draw_list()
        pygame.display.update()