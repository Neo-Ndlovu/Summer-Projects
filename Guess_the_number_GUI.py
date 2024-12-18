import tkinter as tk
from tkinter import messagebox
import random

# Function to start the game with a random number within a range
def start_game():
    # Range for the number (1-100)
    global target_number
    target_number = random.randint(1, 100)
    
    # Calculate the length of the number
    number_length = len(str(target_number))
    
    # Reset attempt count
    global attempts
    attempts = 0
    
    # Update the label to show instructions with the length of the number
    instruction_label.config(text=f"Guess a number between 1 and 100. The number has {number_length} digits:")
    
    # Clear feedback
    feedback_label.config(text="")
    
    # Enable the guess button in case it's disabled
    guess_button.config(state=tk.NORMAL)

# Function to handle the guess and provide feedback
def check_guess():
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    global attempts
    attempts += 1

    if guess < target_number:
        feedback_label.config(text="Too low! Try again.")
    elif guess > target_number:
        feedback_label.config(text="Too high! Try again.")
    else:
        messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {attempts} attempts.")
        feedback_label.config(text="Game Over! You guessed the number.")
        # Disable the guess button after correct guess
        guess_button.config(state=tk.DISABLED)

# Function to restart the game
def restart_game():
    # Restart the game by calling start_game function
    start_game()

# Create the main window
root = tk.Tk()
root.title("Guess The Number Game")

# Global variables
target_number = None
attempts = 0

# Label for instructions
instruction_label = tk.Label(root, text="Click 'Start Game' to begin", font=("Arial", 14))
instruction_label.pack(pady=10)

# Entry widget to input guesses
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Label for feedback on guesses
feedback_label = tk.Label(root, text="", font=("Arial", 14))
feedback_label.pack(pady=10)

# Button to check the guess
guess_button = tk.Button(root, text="Check Guess", font=("Arial", 14), command=check_guess)
guess_button.pack(pady=10)

# Button to start a new game
start_button = tk.Button(root, text="Start Game", font=("Arial", 14), command=start_game)
start_button.pack(pady=10)

# Button to restart the game
restart_button = tk.Button(root, text="Restart Game", font=("Arial", 14), command=restart_game)
restart_button.pack(pady=10)

# Start the game when the window opens
start_game()

# Run the application
root.mainloop()


