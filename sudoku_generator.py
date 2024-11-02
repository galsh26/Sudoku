from sudoku_board import SudokuBoard
import random

from sudoku_solver import SudokuSolver


class SudokuGenerator:
    def __init__(self, difficulty="medium", size=9):
        self.difficulty = difficulty
        self.size = size
        self.board = SudokuBoard(size=size)

    def generate_full_board(self):
        """
        Fills the board with a complete, valid Sudoku solution using backtracking.
        """
        self.fill_board()
        return SudokuBoard(self.size, [row[:] for row in self.board.board])

    def fill_board(self):
        # Backtracking algorithm adapted for variable board size
        for row in range(self.size):
            for col in range(self.size):
                if self.board.board[row][col] == 0:
                    numbers = list(range(1, self.size + 1))
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.board.is_valid_move(row, col, num):
                            self.board.board[row][col] = num
                            if self.fill_board():
                                return True
                            self.board.board[row][col] = 0
                    return False
        return True

    def generate_puzzle(self):
        """
        Generates a puzzle by first creating a full board and then removing numbers based on difficulty.
        """
        # First generate a complete board
        self.generate_full_board()

        # Then remove numbers to create the puzzle
        self.remove_numbers_from_board()
        return self.board

    def remove_numbers_from_board(self):
        """
        Removes numbers from the board to create a puzzle with a unique solution based on difficulty.
        """
        cells_to_remove = int({"easy": 0.3, "medium": 0.4, "hard": 0.5}[self.difficulty] * (self.size ** 2))
        removed_cells = 0
        while removed_cells < cells_to_remove:
            row, col = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if self.board.board[row][col] != 0:
                # Save the value and remove the cell
                removed_value = self.board.board[row][col]
                self.board.board[row][col] = 0

                # Check if board still has a unique solution
                temp_solver = SudokuSolver(SudokuBoard(self.size, [row[:] for row in self.board.board]))
                if temp_solver.solve():
                    removed_cells += 1
                else:
                    # Restore if it creates multiple solutions
                    self.board.board[row][col] = removed_value
