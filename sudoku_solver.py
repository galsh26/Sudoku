class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.size = board.size
        self.subgrid_rows = board.subgrid_rows
        self.subgrid_cols = board.subgrid_cols

    def solve(self):
        """
        Solves the Sudoku puzzle using backtracking.
        """
        empty = self.find_empty_cell()
        if not empty:
            return True  # Puzzle solved
        row, col = empty

        for num in range(1, self.size + 1):
            if self.board.is_valid_move(row, col, num):
                self.board.board[row][col] = num

                if self.solve():
                    return True

                # Undo the move if it leads to an invalid state
                self.board.board[row][col] = 0

        return False

    def find_empty_cell(self):
        """
        Finds an empty cell in the board (represented by 0).
        Returns a tuple (row, col) if an empty cell is found, else None.
        """
        for row in range(self.size):
            for col in range(self.size):
                if self.board.board[row][col] == 0:
                    return (row, col)
        return None
