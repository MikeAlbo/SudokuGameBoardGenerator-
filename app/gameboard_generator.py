from random import sample
from app.utils import print_board


# bord builder
# board generating algorithm from -->
# https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python


base = 3
side = base*base


# pattern for a baseline valid solution
def pattern(r, c): return (base*(r % base)+r//base+c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s, len(s))


def generate_board():
    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


# takes in the number of boards to be generated and returns a list of game board objects
# game board object = {"id" : [<list of row list>]}
def generate_list_of_boards(length):
    board_list = []
    for index in range(length):
        new_board = generate_board()
        print(index)
        print_board(new_board)
        board_id = index + 1
        board_set = {"board_id": board_id, "game_board": new_board}
        board_list.append(board_set)
    return board_list
