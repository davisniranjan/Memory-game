import random
import time
import tkinter as tk

# Define the game window
window = tk.Tk()
window.geometry("300x150")
window.title("Memory Game")

# Define the game variables
sequence = []
user_sequence = []
level = 1
score = 0
game_started = False

# Define the game functions
def generate_sequence():
    global sequence
    sequence = [random.randint(1, 9) for _ in range(level)]
    show_sequence()

def show_sequence():
    global game_started
    game_started = True
    message_label.config(text="Memorize the sequence!")
    for num in sequence:
        button = buttons[num-1]
        button.config(bg="white")
        window.update()
        time.sleep(1)
        button.config(bg="gray")
        window.update()
        time.sleep(0.5)
    message_label.config(text="Enter the sequence!")
    clear_user_sequence()

def clear_user_sequence():
    global user_sequence
    user_sequence = []

def check_sequence():
    global level, score, game_started
    if user_sequence == sequence:
        message_label.config(text="Correct!")
        level += 1
        score += 10
        level_label.config(text=f"Level: {level}")
        score_label.config(text=f"Score: {score}")
        game_started = False
        generate_sequence()
    else:
        message_label.config(text="Wrong! Try again.")
        clear_user_sequence()

def button_click(num):
    global game_started
    if game_started:
        user_sequence.append(num)
        button = buttons[num-1]
        button.config(bg="white")
        window.update()
        time.sleep(0.2)
        button.config(bg="gray")
        window.update()
        if len(user_sequence) == level:
            check_sequence()

# Define the game widgets
message_label = tk.Label(window, text="Press start to begin.")
message_label.pack()

buttons_frame = tk.Frame(window)
buttons_frame.pack()

buttons = []
for i in range(1, 10):
    button = tk.Button(buttons_frame, text=str(i), width=3, height=2, bg="gray",
                       command=lambda num=i: button_click(num))
    button.grid(row=(i-1)//3, column=(i-1)%3)
    buttons.append(button)

start_button = tk.Button(window, text="Start", width=8, height=2,
                         command=generate_sequence)
start_button.pack(side=tk.LEFT, padx=10)

quit_button = tk.Button(window, text="Quit", width=8, height=2,
                        command=window.quit)
quit_button.pack(side=tk.RIGHT, padx=10)

level_label = tk.Label(window, text="Level: 1")
level_label.pack()

score_label = tk.Label(window, text="Score: 0")
score_label.pack()

# Start the game
window.mainloop()

