import json
import os
import subprocess
import platform
import sys

path = "/"


# determine the OS and opens a file by the given file path
# todo: add try/ except and handle the error
def open_file(file_path):
    if platform.system() == "Darwin":   # Mac
        subprocess.call(('open', file_path))
    elif platform.system() == 'Windows':  # Windows
        os.startfile(file_path)
    else:  # linux variants
        subprocess.call(('xdg-open', file_path))


# handle the file selection with the proper suffix for .md or .json
# will clean up user input if they add/ neglect the file type
def select_open_file(directory, file):
    no_suffix = remove_suffix(file)
    if no_suffix.upper() == "README":
        return open_file("README.md")
    else:
        return open_file("%s/%s.json" % (directory, no_suffix))


# removes the given suffix from the input
def remove_suffix(filename):
    return os.path.splitext(filename)[0]


# the sequence for exiting a program
def input_error_seq(error_message, action):
    print(error_message)
    input("Press ENTER to exit app...")
    print("\n----------------------------\n")
    action()


# convert to JSON
def convert_to_json(game_board_object):
    return json.dumps(game_board_object)


# check if filename exist in directory
def file_exist(directory, filename, ext):
    for file in os.listdir(directory):
        if file == "%s%s" % (filename, ext):
            return True
    return False


# check if directory exist
def make_dir(directory):
    dir_path = str(directory)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# prints a single board
def print_board(game_board):
    for row in game_board:
        print(row)
    print("\n ------- \n")


# writes the new file to the given directory
def write_file(directory, filename, ext, content):
    file_path = directory + "/" + filename + "." + ext
    file = open(file_path, "w")
    file.write(content)
    file.close()


# prints all the boards from a list of boards
def print_game_boards(game_boards):
    for game_board in game_boards:
        for board in game_board:
            for row in game_board[board]:
                print(row)
        print("\n ------- \n")


# prints a game board json file
def print_from_file(directory, filename):
    full_file_name = "%s.json" % remove_suffix(filename)
    with open("%s/%s" % (directory, full_file_name)) as f:
        data = json.load(f)
        print_game_boards(data)
    sys.exit()
