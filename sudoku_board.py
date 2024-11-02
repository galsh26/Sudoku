class SudokuBoard:
    def __init__(self, size=9, board=None):
        # Initialize the board with the specified size (default is 9x9)
        self.size = size
        self.subgrid_rows, self.subgrid_cols = self.get_subgrid_shape(size)

        # If no initial board is provided, create an empty board
        if board:
            self.board = board
        else:
            self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def get_subgrid_shape(self, size):
        """
        Determines the subgrid shape based on board size.
        """
        if size == 6:
            return 2, 3
        elif size == 16:
            return 4, 4
        else:
            return 3, 3

    def is_valid_move(self, row, col, num):
        """
        Checks if placing 'num' at position (row, col) is valid according to Sudoku rules.
        """
        # Check row
        for x in range(self.size):
            if self.board[row][x] == num:
                return False

        # Check column
        for y in range(self.size):
            if self.board[y][col] == num:
                return False

        # Check subgrid
        start_row = (row // self.subgrid_rows) * self.subgrid_rows
        start_col = (col // self.subgrid_cols) * self.subgrid_cols
        for i in range(self.subgrid_rows):
            for j in range(self.subgrid_cols):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def place_number(self, row, col, num):
        """
        Places 'num' at position (row, col) if it's valid, otherwise returns False.
        """
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
            return True
        return False

    def remove_number(self, row, col):
        """
        Removes a number from a specific position and resets it to zero.
        """
        self.board[row][col] = 0

    def print_board(self):
        """
        Prints the board in a readable format.
        """
        for i in range(self.size):
            if i % self.subgrid_rows == 0 and i != 0:
                print("-" * (self.size * 2 + self.subgrid_cols - 1))
            for j in range(self.size):
                if j % self.subgrid_cols == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j] if self.board[i][j] != 0 else ".", end=" ")
            print()
