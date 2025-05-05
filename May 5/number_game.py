import tkinter as tk
import random

# Function to start a new game
def start_new_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    result_var.set("Guess a number between 1 and 100.")
    attempts_var.set(f"Attempts: {attempts}")
    entry_guess.delete(0, tk.END)  # Clear the input field

# Function to check the user's guess
def check_guess():
    try:
        guess = int(entry_guess.get())  # Get the user's guess
    except ValueError:
        result_var.set("Please enter a valid number.")
        return
    
    global attempts
    attempts += 1
    
    if guess < number_to_guess:
        result_var.set("Too low! Try again.")
    elif guess > number_to_guess:
        result_var.set("Too high! Try again.")
    else:
        result_var.set(f"Correct! The number was {number_to_guess}. You took {attempts} attempts.")
    
    attempts_var.set(f"Attempts: {attempts}")

# Create main window
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x300")  # Set the window size
window.config(bg="#ecf0f1")  # Background color of window

# Initialize variables
number_to_guess = random.randint(1, 100)
attempts = 0

# Create input field for guessing
entry_guess = tk.Entry(window, width=10, font=("Arial", 14), bd=5, relief="solid", justify="center")
entry_guess.grid(row=0, column=0, padx=10, pady=10)

# Create button to check the guess
button_check = tk.Button(window, text="Check Guess", font=("Arial", 14), bd=5, relief="raised", bg="#2980b9", fg="white", command=check_guess)
button_check.grid(row=0, column=1, padx=10, pady=10)

# Create label to display result
result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Arial", 14), bg="#34495e", fg="white", width=30, height=2, wraplength=380)
result_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create label to display the number of attempts
attempts_var = tk.StringVar()
attempts_label = tk.Label(window, textvariable=attempts_var, font=("Arial", 12), bg="#ecf0f1", fg="black", width=30)
attempts_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create button to start a new game
button_new_game = tk.Button(window, text="Start New Game", font=("Arial", 14), bd=5, relief="raised", bg="#27ae60", fg="white", command=start_new_game)
button_new_game.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

# Run the main loop
window.mainloop()
