import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import random
import time

class XOGame:
    def __init__(self):
        # Initialize main window
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("XO Game - Ultimate Edition")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        
        # Game variables
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_active = True
        self.scores = {"X": 0, "O": 0, "Ties": 0}
        self.player_x_color = "#FF4B4B"  # Red
        self.player_o_color = "#4B93FF"  # Blue
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        # Title frame
        title_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        title_frame.pack(pady=10)
        
        title = ctk.CTkLabel(title_frame, text="XO Game", 
                            font=ctk.CTkFont(size=28, weight="bold"))
        title.pack()
        
        subtitle = ctk.CTkLabel(title_frame, text="Ultimate Edition", 
                               font=ctk.CTkFont(size=14))
        subtitle.pack()
        
        # Score display
        score_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        score_frame.pack(pady=10)
        
        ctk.CTkLabel(score_frame, text="Scores", 
                    font=ctk.CTkFont(size=16, weight="bold")).pack()
        
        score_inner_frame = ctk.CTkFrame(score_frame, fg_color="transparent")
        score_inner_frame.pack(pady=5)
        
        self.x_score_label = ctk.CTkLabel(score_inner_frame, text=f"X: {self.scores['X']}", 
                                         text_color=self.player_x_color,
                                         font=ctk.CTkFont(size=14, weight="bold"))
        self.x_score_label.pack(side=tk.LEFT, padx=10)
        
        self.tie_score_label = ctk.CTkLabel(score_inner_frame, text=f"Ties: {self.scores['Ties']}", 
                                           font=ctk.CTkFont(size=14))
        self.tie_score_label.pack(side=tk.LEFT, padx=10)
        
        self.o_score_label = ctk.CTkLabel(score_inner_frame, text=f"O: {self.scores['O']}", 
                                         text_color=self.player_o_color,
                                         font=ctk.CTkFont(size=14, weight="bold"))
        self.o_score_label.pack(side=tk.LEFT, padx=10)
        
        # Game board
        board_frame = ctk.CTkFrame(self.root)
        board_frame.pack(pady=20)
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ctk.CTkButton(
                    board_frame, 
                    text="", 
                    width=100, 
                    height=100,
                    font=ctk.CTkFont(size=32, weight="bold"),
                    fg_color="#2B2B2B",
                    hover_color="#3B3B3B",
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row.append(button)
            self.buttons.append(row)
        
        # Current player indicator
        self.turn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.turn_frame.pack(pady=10)
        
        self.turn_label = ctk.CTkLabel(
            self.turn_frame, 
            text=f"Current Player: X", 
            text_color=self.player_x_color,
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.turn_label.pack()
        
        # Control buttons
        control_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        control_frame.pack(pady=20)
        
        restart_btn = ctk.CTkButton(
            control_frame, 
            text="Restart Game", 
            command=self.reset_game,
            fg_color="#2B2B2B",
            hover_color="#3B3B3B"
        )
        restart_btn.pack(side=tk.LEFT, padx=10)
        
        new_game_btn = ctk.CTkButton(
            control_frame, 
            text="New Game", 
            command=self.new_game,
            fg_color="#2B2B2B",
            hover_color="#3B3B3B"
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        # Theme switcher
        theme_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        theme_frame.pack(pady=10)
        
        ctk.CTkLabel(theme_frame, text="Theme:").pack(side=tk.LEFT, padx=5)
        
        self.theme_var = ctk.StringVar(value="dark")
        theme_option = ctk.CTkOptionMenu(
            theme_frame, 
            values=["dark", "light", "system"],
            command=self.change_theme,
            variable=self.theme_var
        )
        theme_option.pack(side=tk.LEFT, padx=5)
        
        # Player colors
        color_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        color_frame.pack(pady=10)
        
        ctk.CTkLabel(color_frame, text="X Color:").pack(side=tk.LEFT, padx=5)
        x_color_option = ctk.CTkOptionMenu(
            color_frame, 
            values=["Red", "Green", "Purple", "Orange"],
            command=self.change_x_color
        )
        x_color_option.pack(side=tk.LEFT, padx=5)
        
        ctk.CTkLabel(color_frame, text="O Color:").pack(side=tk.LEFT, padx=5)
        o_color_option = ctk.CTkOptionMenu(
            color_frame, 
            values=["Blue", "Teal", "Pink", "Yellow"],
            command=self.change_o_color
        )
        o_color_option.pack(side=tk.LEFT, padx=5)
    
    def change_theme(self, choice):
        ctk.set_appearance_mode(choice)
    
    def change_x_color(self, color):
        color_map = {
            "Red": "#FF4B4B",
            "Green": "#4BAF50",
            "Purple": "#9B59B6",
            "Orange": "#F39C12"
        }
        self.player_x_color = color_map[color]
        self.update_ui()
    
    def change_o_color(self, color):
        color_map = {
            "Blue": "#4B93FF",
            "Teal": "#1ABC9C",
            "Pink": "#E91E63",
            "Yellow": "#F1C40F"
        }
        self.player_o_color = color_map[color]
        self.update_ui()
    
    def update_ui(self):
        # Update score labels
        self.x_score_label.configure(text=f"X: {self.scores['X']}", 
                                    text_color=self.player_x_color)
        self.o_score_label.configure(text=f"O: {self.scores['O']}", 
                                    text_color=self.player_o_color)
        self.tie_score_label.configure(text=f"Ties: {self.scores['Ties']}")
        
        # Update turn label
        if self.current_player == "X":
            self.turn_label.configure(text="Current Player: X", 
                                     text_color=self.player_x_color)
        else:
            self.turn_label.configure(text="Current Player: O", 
                                     text_color=self.player_o_color)
        
        # Update board buttons
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "X":
                    self.buttons[i][j].configure(text="X", 
                                                text_color=self.player_x_color,
                                                state="disabled")
                elif self.board[i][j] == "O":
                    self.buttons[i][j].configure(text="O", 
                                                text_color=self.player_o_color,
                                                state="disabled")
                else:
                    self.buttons[i][j].configure(text="", state="normal")
    
    def make_move(self, row, col):
        if not self.game_active or self.board[row][col] != "":
            return
        
        # Make the move
        self.board[row][col] = self.current_player
        
        # Check for win or tie
        if self.check_winner():
            self.scores[self.current_player] += 1
            self.show_winner()
            self.game_active = False
        elif self.is_board_full():
            self.scores["Ties"] += 1
            self.show_tie()
            self.game_active = False
        else:
            # Switch player
            self.current_player = "O" if self.current_player == "X" else "X"
        
        # Update UI
        self.update_ui()
        
        # AI move if it's O's turn and game is still active
        if self.current_player == "O" and self.game_active:
            self.root.after(500, self.ai_move)
    
    def ai_move(self):
        # Simple AI: try to win, then block, then random move
        # Check for winning move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    if self.check_winner():
                        self.make_ai_move(i, j)
                        return
                    self.board[i][j] = ""
        
        # Check for blocking move
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "X"
                    if self.check_winner():
                        self.board[i][j] = "O"
                        self.make_ai_move(i, j)
                        return
                    self.board[i][j] = ""
        
        # If center is available, take it
        if self.board[1][1] == "":
            self.make_ai_move(1, 1)
            return
        
        # Otherwise, random move
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.make_ai_move(row, col)
    
    def make_ai_move(self, row, col):
        self.board[row][col] = "O"
        
        if self.check_winner():
            self.scores["O"] += 1
            self.show_winner()
            self.game_active = False
        elif self.is_board_full():
            self.scores["Ties"] += 1
            self.show_tie()
            self.game_active = False
        else:
            self.current_player = "X"
        
        self.update_ui()
    
    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
        
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        
        return False
    
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True
    
    def show_winner(self):
        winner = self.current_player
        color = self.player_x_color if winner == "X" else self.player_o_color
        
        # Create a custom dialog
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Game Over")
        dialog.geometry("300x200")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
        
        ctk.CTkLabel(dialog, text="Game Over!", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
        ctk.CTkLabel(dialog, text=f"Player {winner} wins!", 
                    text_color=color,
                    font=ctk.CTkFont(size=16)).pack(pady=10)
        
        def close_dialog():
            dialog.destroy()
            dialog.grab_release()
        
        ctk.CTkButton(dialog, text="OK", command=close_dialog).pack(pady=20)
    
    def show_tie(self):
        # Create a custom dialog
        dialog = ctk.CTkToplevel(self.root)
        dialog.title("Game Over")
        dialog.geometry("300x200")
        dialog.resizable(False, False)
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")
        
        ctk.CTkLabel(dialog, text="Game Over!", 
                    font=ctk.CTkFont(size=20, weight="bold")).pack(pady=20)
        
        ctk.CTkLabel(dialog, text="It's a tie!", 
                    font=ctk.CTkFont(size=16)).pack(pady=10)
        
        def close_dialog():
            dialog.destroy()
            dialog.grab_release()
        
        ctk.CTkButton(dialog, text="OK", command=close_dialog).pack(pady=20)
    
    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.game_active = True
        self.update_ui()
    
    def new_game(self):
        self.scores = {"X": 0, "O": 0, "Ties": 0}
        self.reset_game()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = XOGame()
    game.run()