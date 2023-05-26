import random
import tkinter as tk
from tkinter import messagebox

# Function to read multiple-choice questions from a text file
def read_questions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    questions = []
    i = 0
    while i < len(lines):
        question = lines[i].strip()
        options = [lines[i+1].strip(), lines[i+2].strip(), lines[i+3].strip(), lines[i+4].strip()]
        answer_line = lines[i+5].strip().split(": ")
        if len(answer_line) == 2 and answer_line[0].lower() == "answer":
            answer = answer_line[1]
            questions.append((question, options, answer))
        i += 6

    return questions


# Function to handle user's answer and check correctness
def check_answer(window, questions, question, options, answer, user_answer):
    user_answer = chr(ord('A') + user_answer)  # Convert index back to corresponding letter (A, B, C, D)
    if user_answer == answer:
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showinfo("Incorrect!", f"Sorry, your answer is incorrect. The correct answer is: {answer}")

    window.destroy()  # Close the current question window
    ask_question(questions)  # Ask a new question


# Function to ask a random multiple-choice question
def ask_question(questions):
    question, options, answer = random.choice(questions)

    # Create a new Tkinter window
    window = tk.Toplevel()
    window.title("Trivia Game")

    # Create question label
    question_label = tk.Label(window, text=question, wraplength=300)
    question_label.pack()

    # Create option buttons
    for i, option in enumerate(options):
        option_button = tk.Button(window, text=option, command=lambda idx=i: check_answer(window, questions, question, options, answer, idx))
        option_button.pack()

    # Add quit button
    quit_button = tk.Button(window, text="Quit", command=window.destroy)
    quit_button.pack()

    # Center the window
    window.eval('tk::PlaceWindow . center')


# Main game loop
def trivia_game(file_path):
    questions = read_questions(file_path)

    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Trivia Game")

    # Create game instructions label
    instructions_label = tk.Label(root, text="Welcome to the Trivia Game!\nI will ask you some multiple-choice questions, and you have to select the correct answer.")
    instructions_label.pack()

    # Create start button
    start_button = tk.Button(root, text="Start Game", command=lambda: ask_question(questions))
    start_button.pack()

    # Add quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack()

    # Center the window
    root.eval('tk::PlaceWindow . center')

    # Start the Tkinter event loop
    root.mainloop()


# Specify the file path to your text file containing questions and answers
file_path = "questions.txt"

# Start the trivia game
trivia_game(file_path)
