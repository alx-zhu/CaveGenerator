import random
import math

# Original Ideas: http://pixelenvy.ca/wa/ca_cave.html
# http://roguebasin.com/index.php/Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels
# All Code Written By Alexander Zhu. Original concepts from sources cited above
# but no code was copied from these sources.
space = '.'
wall = '#'

# creates an initial map before cell automata cycle with floor_ratio of 
# all squares as spaces.
def create_initial(rows, cols, space_ratio):
    #floor ratio is a ratio out of 1
    cave = [[wall]*cols for row in range(rows)]
    count = 0
    while (count < (space_ratio*rows*cols)):
        rand_index = random.randint(1, rows*cols-1)
        row = rand_index//cols
        col = rand_index%cols
        if (0 < row and row < rows-1 and 0 < col and col < rows-1
            and cave[row][col] != space):
            cave[row][col] = space
            count += 1
    return cave

# returns true if a given row and col are not out of bounds, and are not 
# the outside layer of walls.
def is_valid_rowcol(cave, row, col):
    rows = len(cave)
    cols = len(cave[0])
    if (0 < row and row < rows-1 and 0 < col and col < cols-1):
        return True
    return False

# uses 4-5 rule. If has less than 4 surrounding walls, cell becomes space.
# If has more than 5 surrounding walls, cell becomes wall. Otherwise, no change.
def cell_automata_1step(cave, row, col):
    # count 1 for squares 1 space away
    count1 = 0
    # first, count squares 1 step away
    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if (is_valid_rowcol(cave, row+drow, col+dcol) and
                cave[row+drow][col+dcol] == wall):
                count1 += 1
    if (count1 >= 5): cave[row][col] = wall
    else: cave[row][col] = space

def cell_automata_2step(cave, row, col):
    # count 1 for squares 1 space away
    count1 = 0
    # count 2 for squares 2 spaces away
    count2 = 0
    # first, count squares 1 step away
    for drow in [-1, 0, 1]:
        for dcol in [-1, 0, 1]:
            if (is_valid_rowcol(cave, row+drow, col+dcol) and
                cave[row+drow][col+dcol] == wall):
                count1 += 1
    # now, count squares 2 steps away
    for drow in [-2, 0, 2]:
        for dcol in [-2, 0, 2]:
            if (is_valid_rowcol(cave, row+drow, col+dcol) and
                cave[row+drow][col+dcol] == wall):
                count2 += 1
    if (count1 >= 5 or count2 <= 1): cave[row][col] = wall
    else: cave[row][col] = space

# runs one cellular automata cycle
def run_CA_cycle_1step(cave, rows, cols):
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            cell_automata_1step(cave, row, col)

# runs one cellular automata cycle
def run_CA_cycle_2step(cave, rows, cols):
    for row in range(1, rows-1):
        for col in range(1, cols-1):
            cell_automata_2step(cave, row, col)

def print_cave(cave):
    rows = len(cave)
    cols = len(cave[0])
    for row in range(rows):
        for col in range(cols):
            print(f"{cave[row][col]}", end = " ")
        print()

def main():
    cave = create_initial(50, 50, 0.45)
    for i in range(3):
        run_CA_cycle_2step(cave, len(cave), len(cave[0]))
    for i in range(2):
        run_CA_cycle_1step(cave, len(cave), len(cave[0]))
    print_cave(cave)

main()