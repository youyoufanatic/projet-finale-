import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("400x450")
        
        
        self.turn = 'X'
        self.board = [""] * 9
        self.game_over = False
        self.buttons = []

        
        self.create_widgets()
        
    def create_widgets(self):
        
        self.status_label = tk.Label(
            self.window, 
            text=f"Player {self.turn}'s Turn", 
            font=("Arial", 16)
        )
        self.status_label.pack(pady=10)

        
        frame = tk.Frame(self.window)
        frame.pack()

        
        for i in range(9):
            btn = tk.Button(
                frame, 
                text="", 
                font=("Arial", 20, "bold"), 
                width=5, 
                height=2,
                command=lambda i=i: self.on_click(i)
            )
            
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        
        restart_btn = tk.Button(
            self.window, 
            text="Restart Game", 
            font=("Arial", 12), 
            bg="lightblue",
            command=self.reset_game
        )
        restart_btn.pack(pady=20)

    def on_click(self, index):
        """Handles a button click."""
        if self.board[index] == "" and not self.game_over:
            
            self.board[index] = self.turn
            
            
            self.buttons[index].config(
                text=self.turn, 
                fg="blue" if self.turn == "X" else "red"
            )
            
            
            if self.check_winner():
                self.status_label.config(text=f"Player {self.turn} Wins!", fg="green")
                self.game_over = True
                messagebox.showinfo("Game Over", f"Player {self.turn} Wins!")
            elif "" not in self.board:
                self.status_label.config(text="It's a Tie!", fg="orange")
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a Tie!")
            else:
                
                self.turn = "O" if self.turn == "X" else "X"
                self.status_label.config(text=f"Player {self.turn}'s Turn", fg="black")

    def check_winner(self):
        """Checks the board for a winning combination."""
        winning_combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), 
            (0, 3, 6), (1, 4, 7), (2, 5, 8), 
            (0, 4, 8), (2, 4, 6)             
        ]
        
        for a, b, c in winning_combos:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                self.highlight_winner(a, b, c)
                return True
        return False

    def highlight_winner(self, a, b, c):
        """Changes the background color of the winning buttons."""
        for index in [a, b, c]:
            self.buttons[index].config(bg="lightgreen")

    def reset_game(self):
        """Resets the board for a new game."""
        self.turn = 'X'
        self.board = [""] * 9
        self.game_over = False
        self.status_label.config(text=f"Player {self.turn}'s Turn", fg="black")
        
        for btn in self.buttons:
            btn.config(text="", bg="SystemButtonFace", state="normal")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()