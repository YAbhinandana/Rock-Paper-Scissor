import tkinter as tk
import random
from tkinter import messagebox

choices = ['rock', 'paper', 'scissors']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    
    user_choice_label.config(text=f"Your choice: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice.capitalize()}")
    result_label.config(text=result)

  
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1
    score_label.config(text=f"Your score: {user_score} | Computer's score: {computer_score}")

 
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="")
    score_label.config(text=f"Your score: 0 | Computer's score: 0")

user_score = 0
computer_score = 0

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("600x400")

# Add labels and buttons
welcome_label = tk.Label(window, text="Rock-Paper-Scissors Game", font=("Times New Roman", 20))
welcome_label.pack(pady=10)

user_choice_label = tk.Label(window, text="Your choice: ", font=("Times New Roman", 14))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(window, text="Computer's choice: ", font=("Times New Roman", 14))
computer_choice_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Times New Roman", 16))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Your score: 0 | Computer's score: 0", font=("Times New Roman", 14))
score_label.pack(pady=10)

# Buttons for rock, paper, and scissors
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Reset button
reset_button = tk.Button(window, text="Reset Game", width=40, command=reset_game)
reset_button.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()
