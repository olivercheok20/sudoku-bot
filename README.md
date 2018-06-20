# sudoku-bot
Implementation of the backtracking Sudoku-solving algorithm in Python

Follow the following steps to run the program successfully:

1. Convert Sudoku board to be solved to a list of positions and values.

Each square on the Sudoku board is given an index, starting from 0 in the leftmost square in the top row and ending with 80 in the rightmost square in the bottom row. Index increases linearly from left to right across each row, continuing at the beginning each row from the end of the previous one. For each number in the unsolved board, indicate its position (index) and value. 

(E.g. if the 4th square in the 2nd row is a '2', index is 12 and value is 2)

2. Run the sudoku_backtrack.py file in your terminal

After navigating to the directory containing the sudoku_backtrack.py file from your Terminal, run the program with the following command:

> python3 sudoku_backtrack.py --positions (singly-spaced positions) --values (singly-spaced values)

Ensure that the number of positions matches the number of values and that the order of positions given corresponds to the order of values given.
