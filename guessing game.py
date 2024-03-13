import random
import tkinter as tk
from tkinter import messagebox

high_score = float('inf')

def start_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text="")
    high_score_label.config(text=f"High Score: {high_score}")

def check_guess():
    global attempts, high_score
    guess = int(guess_entry.get())
    attempts += 1

    if guess < secret_number:
        result_label.config(text="Too low! Try again.")
    elif guess > secret_number:
        result_label.config(text="Too high! Try again.")
    else:
        high_score = min(high_score, attempts)
        messagebox.showinfo("Congratulations!", f"You guessed the number {secret_number} in {attempts} attempts.")
        high_score_label.config(text=f"High Score: {high_score}")
        start_game()

# Create the main window
root = tk.Tk()
root.title("Guessing Game")

# Create the game frame
game_frame = tk.Frame(root)
game_frame.pack(pady=20)

# Create the start button
start_button = tk.Button(game_frame, text="Start Game", command=start_game)
start_button.pack(pady=10)

# Create the guess entry
guess_entry = tk.Entry(game_frame, font=("Arial", 14))
guess_entry.pack(pady=5)

# Create the check button
check_button = tk.Button(game_frame, text="Check Guess", command=check_guess)
check_button.pack(pady=5)

# Create the result label
result_label = tk.Label(game_frame, font=("Arial", 12), fg="green")
result_label.pack(pady=10)

high_score_label = tk.Label(game_frame, font=("Arial", 12), fg="blue")
high_score_label.pack(pady=10)

# Start the main event loop
root.mainloop()