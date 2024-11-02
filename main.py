import tkinter as tk
from tkinter import ttk, messagebox
from ui import SudokuUI

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Main Menu")

        # Initialize settings variables
        self.selected_difficulty = "medium"
        self.selected_board_size = "9x9"

        # Title label
        title_label = ttk.Label(root, text="Welcome to Sudoku Game", font=("Arial", 18))
        title_label.pack(pady=20)

        # Start Game Button
        start_game_button = ttk.Button(root, text="Start Game", command=self.start_game)
        start_game_button.pack(pady=10)

        # Settings Button
        settings_button = ttk.Button(root, text="Game Settings", command=self.open_settings)
        settings_button.pack(pady=10)

    def start_game(self):
        """
        Starts the Sudoku game with current settings.
        """
        self.root.destroy()  # Close the main menu
        game_root = tk.Tk()
        app = SudokuUI(game_root, difficulty=self.selected_difficulty, board_size=self.selected_board_size)
        game_root.mainloop()

    def open_settings(self):
        """
        Opens the settings window for choosing difficulty and board size.
        """
        settings_root = tk.Toplevel(self.root)
        settings_root.title("Game Settings")
        GameSettings(settings_root, self)

class GameSettings:
    def __init__(self, root, main_menu):
        self.root = root
        self.main_menu = main_menu
        self.difficulty = tk.StringVar(value=main_menu.selected_difficulty)
        self.board_size = tk.StringVar(value=main_menu.selected_board_size)

        # Difficulty selection
        difficulty_label = ttk.Label(root, text="Select Difficulty:", font=("Arial", 12))
        difficulty_label.pack(pady=5)
        difficulty_menu = ttk.OptionMenu(root, self.difficulty, "medium", "easy", "medium", "hard")
        difficulty_menu.pack(pady=5)

        # Board size selection
        board_size_label = ttk.Label(root, text="Select Board Size:", font=("Arial", 12))
        board_size_label.pack(pady=5)
        board_size_menu = ttk.OptionMenu(root, self.board_size, "9x9", "6x6", "9x9", "16x16")
        board_size_menu.pack(pady=5)

        # Save settings button
        save_button = ttk.Button(root, text="Save Settings", command=self.save_settings)
        save_button.pack(pady=10)

    def save_settings(self):
        """
        Saves the selected settings to the main menu and closes the settings window.
        """
        self.main_menu.selected_difficulty = self.difficulty.get()
        self.main_menu.selected_board_size = self.board_size.get()
        messagebox.showinfo("Settings Saved", f"Difficulty: {self.difficulty.get()}\nBoard Size: {self.board_size.get()}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()
