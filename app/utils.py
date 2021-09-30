import json
import os

path = "/"


# the sequence for exiting a program
def input_error_seq(error_message, action):
    print(error_message)
    input("Press ENTER to exit app...")
    print("\n----------------------------\n")
    action()

# todo


# convert to JSON
def convert_to_json(game_board_object):
    return json.dumps(game_board_object)


# save JSON to file
# check if filename exist in directory
def file_exist(filename):
    return False if os.path.exists(filename) else True


# check if directory exist
def make_dir(directory):
    dir_path = str(directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def print_board(game_board):
    for row in game_board:
        print(row)
    print("\n ------- \n")


def write_file(directory, filename, ext, content):
    file_path = directory + "/" + filename + "." + ext
    file = open(file_path, "w")
    file.write(content)
    file.close()
