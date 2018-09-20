# ----------------------------------------------
# Conway's Game of Life
# More programs at UsingPython.com/programs
# ----------------------------------------------

import random
import time
import os


# ---------------------------------------------------------------------------

def init_grid(cols, rows, array):
    for i in range(rows):
        array_row = []
        for j in range(cols):
            if i == 0 or j == 0 or (i == rows - 1) or (j == cols - 1):
                array_row += [-1]
            else:
                ran = random.randint(0, 3)
                if ran == 0:
                    array_row += [1]
                else:
                    array_row += [0]
        array += [array_row]


# ---------------------------------------------------------------------------

def print_generation(cols, rows, array, gen_no):
    os.system("cls")

    print("Game of Life -- Generation " + str(gen_no + 1))

    for i in range(rows):
        for j in range(cols):
            if array[i][j] == -1:
                print("#", end=" ")
            elif array[i][j] == 1:
                print("o", end=" ")
            else:
                print(" ", end=" ")
        print("\n")


# ---------------------------------------------------------------------------

def process_next_gen(cols, rows, cur, nxt):
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            nxt[i][j] = process_neighbours(i, j, cur)


# ---------------------------------------------------------------------------

def process_neighbours(x, y, array):
    n_count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if not (i == x and j == y):
                if array[i][j] != -1:
                    n_count += array[i][j]
    if array[x][y] == 1 and n_count < 2:
        return 0
    if array[x][y] == 1 and n_count > 3:
        return 0
    if array[x][y] == 0 and n_count == 3:
        return 1
    else:
        return array[x][y]


# ---------------------------------------------------------------------------
############################################################################
# ---------------------------------------------------------------------------

ROWS = 12
COLS = 55
GENERATIONS = 100
DELAY = 0.2

this_gen = []
next_gen = []

init_grid(COLS, ROWS, this_gen)
init_grid(COLS, ROWS, next_gen)

for gens in range(GENERATIONS):
    print_generation(COLS, ROWS, this_gen, gens)
    process_next_gen(COLS, ROWS, this_gen, next_gen)
    time.sleep(DELAY)
    this_gen, next_gen = next_gen, this_gen
input("Finished. Press <return> to quit.")
