import sys
from app.utils import input_error_seq, make_dir, file_exist
from app.gameboard_generator import generate_list_of_boards

# todo: add option to view files using flags i.e. py3 main.py -view <filename>


def main():
    print('generate a new set of game boards \ngive a file name and how many boards to generate')
    print("to quit, type 'exit'")

    make_dir("demoDir")

    filename = input("filename:  ")

    if filename == "exit":
        sys.exit()

    if len(filename) > 0:
        print("filename: ", filename)
    elif file_exist(filename):
        input_error_seq("file name -> %s <- already exist", filename)
    # todo: fix the flow of this
    else:
        input_error_seq("filename should be more than 1 character", sys.exit)

    number_of_boards = input("number of boards: ")

    if number_of_boards == "exit":
        sys.exit()

    try:
        int(number_of_boards)
        print("Number of boards: ", number_of_boards)
    except ValueError:
        input_error_seq("please enter an integer value (1,5,100,500000000, etc", sys.exit)

    generated_list_of_board = generate_list_of_boards(int(number_of_boards))
    #


# if __name__ == '__main__':
#     # print(board)
#     main()
