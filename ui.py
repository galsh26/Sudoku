import tkinter as tk
from tkinter import ttk, messagebox
from sudoku_generator import SudokuGenerator
from sudoku_solver import SudokuSolver
from sudoku_board import SudokuBoard
import random


class SudokuUI:
    def __init__(self, root, difficulty="medium", board_size="9x9"):
        self.root = root
        self.root.title(f"Sudoku {board_size}")

        # Set board size and cell font size based on chosen settings
        if board_size == "6x6":
            self.size = 6
            self.cell_size = 50
            self.font_size = 18
            self.subgrid_shape = (2, 3)
        elif board_size == "16x16":
            self.size = 16
            self.cell_size = 30
            self.font_size = 10
            self.subgrid_shape = (4, 4)
        else:
            self.size = 9
            self.cell_size = 40
            self.font_size = 16
            self.subgrid_shape = (3, 3)

        self.difficulty = difficulty
        self.cells = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.board = None
        self.solved_board = None
        self.create_ui()
        self.start_new_game()

    def create_ui(self):
        self.board_frame = ttk.Frame(self.root, padding="10")
        self.board_frame.grid(row=1, column=0, columnspan=7, sticky="nsew")

        subgrid_rows, subgrid_cols = self.subgrid_shape
        for r_block in range(0, self.size, subgrid_rows):
            for c_block in range(0, self.size, subgrid_cols):
                subgrid_frame = tk.Frame(self.board_frame, highlightbackground="black", highlightthickness=2)
                subgrid_frame.grid(row=r_block // subgrid_rows, column=c_block // subgrid_cols, padx=2, pady=2)
                for row in range(subgrid_rows):
                    for col in range(subgrid_cols):
                        global_row = r_block + row
                        global_col = c_block + col
                        if global_row < self.size and global_col < self.size:
                            cell = ttk.Entry(subgrid_frame, width=2, justify="center", font=("Arial", self.font_size))
                            cell.grid(row=row, column=col, padx=1, pady=1, ipadx=self.cell_size // 10,
                                      ipady=self.cell_size // 10)
                            self.cells[global_row][global_col] = cell

        solve_button = ttk.Button(self.root, text="Solve", command=self.animate_solution)
        solve_button.grid(row=0, column=1, padx=5, pady=5)
        hint_button = ttk.Button(self.root, text="Hint", command=self.show_hint)
        hint_button.grid(row=0, column=2, padx=5, pady=5)

    def start_new_game(self):
        generator = SudokuGenerator(difficulty=self.difficulty, size=self.size)

        # Generate the full board for hints
        self.solved_board = generator.generate_full_board()

        # Generate the puzzle board based on the solved board
        self.board = generator.generate_puzzle()
        self.update_board_ui()

    def update_board_ui(self):
        for row in range(self.size):
            for col in range(self.size):
                value = self.board.board[row][col]
                cell = self.cells[row][col]
                cell.config(state="normal")
                cell.delete(0, tk.END)
                if value != 0:
                    cell.insert(0, str(value))
                    cell.config(state="disabled")

    def animate_solution(self):
        solver = SudokuSolver(self.board)
        if solver.solve():
            self.animate_fill(0, 0)
        else:
            messagebox.showinfo("Info", "No solution exists for this puzzle.")

    def animate_fill(self, row, col):
        if row >= self.size:
            return
        next_row, next_col = (row, col + 1) if col + 1 < self.size else (row + 1, 0)
        if self.cells[row][col].get() == "":
            value = self.solved_board.board[row][col]
            self.cells[row][col].config(state="normal")
            self.cells[row][col].delete(0, tk.END)
            self.cells[row][col].insert(0, str(value))
            self.cells[row][col].config(state="disabled")
        self.root.after(50, lambda: self.animate_fill(next_row, next_col))

    def show_hint(self):
        empty_cells = [(row, col) for row in range(self.size) for col in range(self.size) if
                       self.cells[row][col].get() == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            correct_value = self.solved_board.board[row][col]
            self.cells[row][col].config(state="normal")
            self.cells[row][col].delete(0, tk.END)
            self.cells[row][col].insert(0, str(correct_value))
            self.cells[row][col].config(state="disabled")
        else:
            messagebox.showinfo("Hint", "No empty cells to show a hint for!")
