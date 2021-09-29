from random import sample


# bord builder
# board generating algorithm from -->
# https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python

# takes in a file name, number of boards and outputs a JSON file with that number of boards and
# ids

base = 3
side = base*base


# pattern for a baseline valid solution
def pattern(r, c): return (base*(r % base)+r//base+c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s, len(s))


rBase = range(base)
rows = [g*base + r for g in shuffle(rBase) for r in shuffle(rBase)]
cols = [g*base + c for g in shuffle(rBase) for c in shuffle(rBase)]
nums = shuffle(range(1, base*base+1))

# produce board using randomized baseline pattern
board = [[nums[pattern(r, c)] for c in cols] for r in rows]


def generate_list_of_boards(length):
    board_dict = {}
    for index in range(length):
        new_board = [[nums[pattern(r, c)] for c in cols] for r in rows]
        id = index + 1
        set = {id: board}