import json
import argparse
import sys
from app.utils import input_error_seq, make_dir, file_exist, write_file, remove_suffix, print_file, select_open_file
from app.gameboard_generator import generate_list_of_boards


def main():
    # setup messages to the user
    print('\n -generate a new set of game boards \n -give a file name and how many boards to generate')
    print(' -file will be stored as JSON, no need to add a file extension')
    print(' -a game board directory will be created inside your current directory if it does not already exist ')
    print(' -game board file will rewrite current files of the same name ')
    print('\n------------------')
    print('\n -p <filename> to console print file')
    print('\n -open <filename> to open file (EX: "-open readme" will open the readme file )')
    print('\n to quit, type "exit"\n------------------\n')

    # hard coded directory name,
    # could be user assigned in the future but would require some sort of recursive file finder
    # current print features would not work
    dir_name = "generatedGameBoards"

    # argument parser for the console flags
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="print a file")  # print a json file
    parser.add_argument("-open", help="opens file")     # open the readme or json file in system defined app
    args = parser.parse_args()

    # handle the -p flag
    try:
        if args.p:
            print_file(dir_name, args.p)
    except FileNotFoundError:
        print("unable to load file")
        sys.exit()

    # handle the -open flag
    try:
        if args.open:
            print("opening: %s" % args.open)
            select_open_file(dir_name, args.open)
            sys.exit()
    except ValueError:
        print("unable to open file")
        sys.exit()

    # creates directory if not exist
    make_dir(dir_name)

    # get filename from user, removes any file type if added
    filename = remove_suffix(input("filename:  "))

    # handle exit and file name errors
    if filename == "exit":
        sys.exit()

    if len(filename) < 1:
        input_error_seq("filename should be more than 1 character", sys.exit)

    if file_exist(dir_name, filename, ".json"):
        err_msg = 'filename "%s.json" already exist' % filename
        input_error_seq(err_msg, sys.exit)

    print("filename: %s.json" % filename)

    # handles number of boards input
    number_of_boards = input("number of boards: ")

    # handles number of boards errors
    if number_of_boards == "exit":
        sys.exit()

    try:
        int(number_of_boards)
        print("Number of boards: ", number_of_boards)
    except ValueError:
        input_error_seq("please enter an integer value (1,5,100,500000000, etc", sys.exit)

    # generates the list of boards based on number request
    generated_list_of_board = generate_list_of_boards(int(number_of_boards))
    # converts the list of boards to json
    boards_converted_to_json = json.dumps(generated_list_of_board)
    # writes the json to a file named by the user
    write_file(dir_name, filename, "json", boards_converted_to_json)

