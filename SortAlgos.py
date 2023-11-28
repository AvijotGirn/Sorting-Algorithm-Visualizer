def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_info.draw_list({j:draw_info.RED, j+1:draw_info.BLACK}, True)
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
            draw_info.draw_list({i-1:draw_info.RED, i:draw_info.BLACK}, True)
            yield True
    return lst