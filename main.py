
import pygame
import random
from SortingAlgo.bubbleSort import bubble_sort
from SortingAlgo.insertionSort import insertion_sort
pygame.init()
from DrawInfo import DrawInformation
from DrawMethods import draw_list,draw



def generate_starting_list(n,min_val,max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val,max_val)
        lst.append(val)
    return lst

def main():
    run=True
    clock=pygame.time.Clock()

    n=50
    min_val=0
    max_val=100

    lst = generate_starting_list(n,min_val,max_val)
    draw_info=DrawInformation(800,600,lst)
    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None
    while run:
        clock.tick(120)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except:
                sorting=False
        else:
            draw(draw_info,sorting_algo_name,ascending)
        draw(draw_info,sorting_algo_name,ascending)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n,min_val,max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator=sorting_algorithm(draw_info,ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending=True
            elif event.key == pygame.K_d and not sorting:
                ascending=False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm=insertion_sort
                sorting_algo_name="Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm=bubble_sort
                sorting_algo_name="Bubble Sort"

    pygame.quit()

if __name__== "__main__":
    main()
