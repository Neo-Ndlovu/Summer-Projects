import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialize the board (3x3 grid)
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.players = ["X", "O"]
        self.turn = 0
        
        # Create the buttons for the board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text=" ", width=10, height=3, font=('Arial', 24), command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)
        
    def make_move(self, i, j):
        """Handles the player's move when a button is clicked."""
        current_player = self.players[self.turn % 2]
        
        # Only allow the move if the cell is empty
        if self.board[i][j] == " ":
            self.board[i][j] = current_player
            self.buttons[i][j].config(text=current_player, state="disabled")  # Disable button after move
            
            # Check for a winner or draw
            winner = self.check_winner()
            if winner:
                if winner == "Draw":
                    messagebox.showinfo("Game Over", "It's a draw!")
                else:
                    messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            else:
                self.turn += 1  # Switch turns
    
    def check_winner(self):
        """Checks for a winner or draw."""
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != " ":
                return self.board[0][i]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != " ":
            return self.board[0][2]
        
        # Check for draw (if no spaces left)
        if all(cell != " " for row in self.board for cell in row):
            return "Draw"
        
        return None  # No winner yet
    
    def reset_game(self):
        """Resets the game for a new round."""
        # Clear the board and re-enable all buttons
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = 0
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")

# Main function to start the game
def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
