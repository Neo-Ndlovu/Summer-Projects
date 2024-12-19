def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner or if the game is a draw."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]  # Column winner

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check for a draw (if no spaces are left)
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None  # No winner yet

def tic_tac_toe():
    """Main function to play the game."""
    # Initialize an empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        current_player = players[turn % 2]
        print(f"Player {current_player}'s turn.")
        
        # Get user input
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        # Validate the move
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = current_player  # Place the player's mark
                print_board(board)

                # Check for a winner
                result = check_winner(board)
                if result:
                    if result == "Draw":
                        print("It's a draw!")
                    else:
                        print(f"Player {result} wins!")
                    break

                # Switch turns
                turn += 1
            else:
                print("Cell is already occupied. Choose another one.")
        else:
            print("Invalid move. Please select a cell within the grid.")

if __name__ == "__main__":
    tic_tac_toe()
