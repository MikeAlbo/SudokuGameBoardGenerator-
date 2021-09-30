import sys
from app.utils import input_error_seq

# todo: add option to view files using flags i.e. py3 main.py -view <filename>
# todo: change the "app" to game_board_builder


def main():
    print('generate a new set of game boards \ngive a file name and how many boards to generate')
    print("to quit, type 'exit'")

    filename = input("filename:  ")

    if filename == "exit":
        sys.exit()

    if len(filename) > 0:
        print("filename: ", filename)
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


# if __name__ == '__main__':
#     # print(board)
#     main()
