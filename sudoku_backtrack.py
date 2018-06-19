import argparse
import time

def get_input_args():
    """
    Retrieves command line arguments created and defined using the argparse
    module. get_input_args() returns these arguments as an ArgumentParser
    object.
    Parameters:
     None - run get_input_args() to retrieve command line arguments
    Returns:
     parser.parse_args() - data structure that stores command line
     arguments
    """

    #Create the ArgumentParser object

    parser = argparse.ArgumentParser()

    #Add arguments to the ArgumentParser object

    parser.add_argument('--positions', type=int, nargs='*',
                        help='positions of values in initialized board (index starts from 0)')

    parser.add_argument('--values', type=int, nargs='*',
                        help='values in initialized board')

    #Return the parse_args object

    return parser.parse_args()

def initialize_board(positions, values):
    """
    Creates a list of 81 lists representing the 9x9 Sudoku board. Each box is
    represented by a list of the form [value, initial, lowest_val]. value
    refers to the number currently in each box; remains 0 if box is empty.
    initial is a boolean: True if the inputted value is part of the initial
    board, False if otherwise. lowest_val is the lowest possible value in each
    box.
    Parameters:
     positions - list of positions of initial values
     values - list of values in initialized board
    Returns:
     board - list of 81 lists of the form (value, initial, lowest_val)
     representing the populated board
    """

    #Create an empty board
    board = [[0, False, 1] for x in range(81)]

    #Populate the empty board with appropriate values
    for position, value in zip(positions, values):
        board[position] = [value, True, 1]

    #Return the populated board
    return board

def display_board(board):
    """
    Prints a 9x9 grid of the populated with current values.
    Parameters:
     board - list of 81 tuples of the form [value, initial, lowest_val]
    returns:
     None
    """

    row = ''

    for i, square in enumerate(board):
        if i % 9 == 8:
            row += str(square[0])
            print(row)
            row = ''
        else:
            row += str(square[0]) + ' '

def check_square(board, position, value):
    """
    Checks whether a value at a certain position is in conflict with other
    values already on the board. First checks for repetition across rows, then
    down columns, and then within 3x3 sectors. check_square returns a boolean:
    True if there is no conflict and False if there is.
    Parameters:
     board - current board configuration
     position - position of value to be checked
     value - value to be checked
    Returns:
     allowed - True if no conflict, False if otherwise
     """

    #Horizontal conflict

    #Determine which row position is in
    row = int((position + 9) / 9)

    #Checks squares in the row for repetition
    for square in range((row - 1) * 9, row * 9):
        #print(square)
        #Skip square if square is same as position
        if square == position:
            continue
        #Check remaining squares
        else:
            if board[square][0] == value:
                return False

    #Vertical conflict

    #Determine which column position is in
    column = position % 9

    #Checks squares in the column for repetition
    for square in [column + 9 * x for x in range(9)]:
        #print(square)
        #Skip square if square is same as position
        if square == position:
            continue
        #Check remaining squares
        else:
            if board[square][0] == value:
                return False

    #Sector conflict

    #Define positions of squares in all sections and compile to a list
    section_1 = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    section_2 = [3, 4, 5, 12, 13, 14, 21, 22, 23]
    section_3 = [6, 7, 8, 15, 16, 17, 24, 25, 26]

    section_4 = [27, 28, 29, 36, 37, 38, 45, 46, 47]
    section_5 = [30, 31, 32, 39, 40, 41, 48, 49, 50]
    section_6 = [33, 34, 35, 42, 43, 44, 51, 52, 53]

    section_7 = [54, 55, 56, 63, 64, 65, 72, 73, 74]
    section_8 = [57, 58, 59, 66, 67, 68, 75, 76, 77]
    section_9 = [60, 61, 62, 69, 70, 71, 78, 79, 80]

    sections = [section_1, section_2, section_3, section_4, section_5, section_6, section_7, section_8, section_9]

    #Determine which section position is in
    for i, section in enumerate(sections):
        if position in section:
            section_idx = i
            break

    #Check for conflict within section

    for square in sections[section_idx]:
        #print(square)
        #Skip square if square is same as position
        if square == position:
            continue
        #Check remaining squares
        else:
            if board[square][0] == value:
                return False

    #Returns True if none of the above result in conflict
    return True

def fill_square(board, square):
    """
    Fills a specified square on the board with the lowest numerical value.

    TO DO: Use recursion to make code more elegant and readable.

    Parameters:
     board - current board configuration
     square - index of square to be filled up
    Returns:
     board - board configuration with specified square filled with lowest
     numerical value; if lowest value is not within 1-9, returns the original
     board without change
     possible - boolean; True if the square is possible to fill, False if
     the square cannot be filled with a number within 1-9
    """

    #Iterates through each value from 1-9 to check if square can be filled
    if check_square(board, square, 1) and board[square][2] <= 1:
        board[square][0] = 1
    else:
        if check_square(board, square, 2) and board[square][2] <= 2:
            board[square][0] = 2
        else:
            if check_square(board, square, 3) and board[square][2] <= 3:
                board[square][0] = 3
            else:
                if check_square(board, square, 4) and board[square][2] <= 4:
                    board[square][0] = 4
                else:
                    if check_square(board, square, 5) and board[square][2] <= 5:
                        board[square][0] = 5
                    else:
                        if check_square(board, square, 6) and board[square][2] <= 6:
                            board[square][0] = 6
                        else:
                            if check_square(board, square, 7) and board[square][2] <= 7:
                                board[square][0] = 7
                            else:
                                if check_square(board, square, 8) and board[square][2] <= 8:
                                    board[square][0] = 8
                                else:
                                    if check_square(board, square, 9) and board[square][2] <= 9:
                                        board[square][0] = 9
                                    else:
                                        return board, False
    return board, True

def prev_square(board, current_square):
    """
    Given a board and index of the current square, prev_square returns the
    index of the previous square that can be filled. Squares with initialized
    values, as they are part of the puzzle, are skipped as they cannot be
    changed. This function is used in backtracking.
    Parameters:
     board - current board configuration
     current_square - index of current square
    returns
     previous_square - index of previous square
    """

    while True:
        #Skips squares with initialized values part of the original puzzle.
        if not board[current_square - 1][1]:
            return current_square - 1
        else:
            return prev_square(board, current_square - 1)

def next_square(board, current_square):
    """
    Given a board and index of the current square, next_square returns the
    index of the next square that can be filled. Squares with initialized
    values, as they are part of the puzzle, are skipped as they cannot be
    changed. This function is used to identify next square to be filled as
    well as to identify the first square to be filled.
    Parameters:
     board - current board configuration
     current_square - index of current square
    returns
     previous_square - index of previous square
    """

    while True:
        #Skips squares with initialized values part of the original puzzle.
        if not board[current_square + 1][1]:
            return current_square + 1
        return next_square(board, current_square + 1)

def solve(board):
    """
    Adopts a depth-first search algorithm to identify the correct solution.
    This is a brute force approach. First, the starting square is identified
    and then printed. Following that, the following loop is continued until the
    last square to be filled is given a value:

    Check if square can be filled with a value without conflict

        a1. Fill the square if possible, printing the index of the square as
            well as a visual representation of the current board.
        a2. If the square being filled is the final square, cut the loop.

        b1. If square cannot be filled, print the current square and then
            identify the previous square to be filled.
        b2. Reset the current square to its initial value of 0, indicating an
            empty board, as well as the lowest value it can take.
        b3. Increase the lowest value of the previous square by 1.

    Parameters:
     board - initial board configuration
    Returns:
     None
    """

    #Identifies index of first square to be solved
    current_square = -1
    current_square = next_square(board, current_square)
    print('First square to be solved:', current_square)

    #Identifies index of the final square to be solved
    last_square = 81
    last_square = prev_square(board, last_square)

    #Runs this loop until the last square is given a value
    while board[last_square][0] == 0:
        #Checks if current square can be filled and fills it if possible
        if fill_square(board, current_square)[1]:
            board = fill_square(board, current_square)[0]
            print('\nCurrent square: {}\n'.format(current_square))
            display_board(board)
            #Cuts the loops if puzzle is completely filled
            if board[last_square][0] != 0:
                break
            #Moves to next square
            current_square = next_square(board, current_square)
        else:
            print('Current square: {}'.format(current_square))
            print('Backtrack to previous square')
            #Resets values (actual and lowest) of current square
            board[current_square][2] = 1
            board[current_square][0] = 0
            #Moves to previous square and increments lowest value by 1
            current_square = prev_square(board, current_square)
            print('Backtracked to {}'.format(current_square))
            board[current_square][2] = board[current_square][0] + 1

def main():
    """
    Main program.
    Parameters:
     None
    Returns:
     None
    """

    #Retrieves initial time
    init_time = time.time()

    #Retrieve command line arguments and stores it in in_args
    in_args = get_input_args()

    #Check if number of positions matches number of values
    if len(in_args.positions) != len(in_args.values):
        print('Error: Number of positions ({}) does not match number of values ({})'.format(len(in_args.positions), len(in_args.values)))
        quit()

    #Populate board with initial values
    board = initialize_board(in_args.positions, in_args.values)

    #Print initial board configuration
    print('  Initial board  \n=================')
    display_board(board)

    #Finds the solution to the board using a depth-first brute force approach
    solve(board)

    #Prints the amount of time taken for the solution to be found (2 decimal places)
    print('\nPuzzle took {0:.2f} seconds to solve'.format(time.time() - init_time))

if __name__ == '__main__':
    main()
