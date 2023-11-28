import random, pygame
from DrawInformation import DrawInformation, pygame
import SortAlgos

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
    draw_info = DrawInformation(1000,800, lst)
    sorting = False
    ascending = True

    sorting_algorithm = SortAlgos.bubble_sort
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
                sorting_algorithm = SortAlgos.insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = SortAlgos.bubble_sort
                sorting_algo_name = "Bubble Sort"

    pygame.quit()


if __name__ == "__main__":
    main()
