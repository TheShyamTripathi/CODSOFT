from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
import json
import random 

def check_answer(user_answer, correct_answer, question_number):
    if user_answer.lower() == correct_answer.lower():
        messagebox.showinfo("Correct!", "Your answer is right!")
        return 1
    else:
        messagebox.showinfo("Wrong!", f"Wrong! The Correct answer is {correct_answer}")
        return 0

def load_questions(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Extract the questions key from the dictionary
            questions = data.get('questions')
            if questions is not None:
                return questions
            else:
                messagebox.showinfo("Error", "Invalid question format in file")
                return []
    except FileNotFoundError:
        messagebox.showinfo("Error", f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        messagebox.showinfo("Error", f"Invalid JSON format in file: {filepath}")
        return []

def next_question():
    global question_index
    global score

    if questions and question_index < len(questions):
        question = questions[question_index]
        question_text.set(f"Question {question_index + 1}: {question['question']}")
        option_text.set("\n".join([f"{i}. {option}" for i, option in enumerate(question['options'], start=1)]))
        question_index += 1
        submit_Btn.config(state=NORMAL)  # Enable the Submit button for the next question
    else:
        messagebox.showinfo("Quiz Over", f"Your final score is: {score}")
        question_index = 0  # Reset question_index when the quiz is over
        submit_Btn.config(state=DISABLED)  # Disable the Submit button
        root.destroy()

def submit_answer():
    global score
    user_answer = answer_entry.get().strip()
    if user_answer:
        correct_answer = questions[question_index - 1]['correctAnswer']
        score += check_answer(user_answer, correct_answer, question_index)
        next_question()
        answer_entry.config(state='normal')
        answer_entry.delete(0, 'end')
        answer_entry(state='normal')
    else:
        messagebox.showinfo("Warning", "Please enter an answer.")
        answer_entry.config(state='normal')
        answer_entry.delete(0, 'end')
        answer_entry(state='normal')

domain_file_paths = {
    "Science": r"C:\Users\Shyam\Desktop\newpython\GUI python\Science.json",
    "General Knowledge": r"C:\Users\Shyam\Desktop\newpython\GUI python\General Knowledge.json",
    "Computer Science": r"C:\Users\Shyam\Desktop\newpython\GUI python\Computerscience.json"
}

def start_quiz(selected_domain):
    global questions
    global question_index
    global score

    # Get the file path based on the selected domain
    filepath = domain_file_paths.get(selected_domain)

    if not filepath:
        messagebox.showinfo("Error", f"No file path found for {selected_domain}")
        return

    questions = load_questions(filepath)

    if not questions:
        print("No questions loaded. Check your JSON file format.")
        return

    # Shuffle the questions to get them in random order
    random.shuffle(questions)

    print("Loaded questions:", questions)  # Add this line for debugging

    question_index = 0
    score = 0
    next_question()

root = tk.Tk()
root.title("Basic Quiz Game")
root.config(bg="#25BCF7")
root.geometry("500x410")
root.resizable(0,0)

# Domain selection
domain_label = tk.Label(root, text="Select Domain:", bg='#25BCF7', fg="White", font=("Helvetica", 19, "bold"))

domain_label.pack(pady=(10, 0))

domain_options = ["General Knowledge", "Science", "Computer Science"]  # Add more domains as needed
selected_domain = tk.StringVar(root)
selected_domain.set(domain_options[0])  # Default domain
domain_menu = tk.OptionMenu(root, selected_domain, *domain_options)
domain_menu.config(bg="#f30cf7", font=("Helvetica", 12,"bold","italic"))
domain_menu.pack(pady=2)

# Define question_text and option_text
question_text = tk.StringVar()
option_text = tk.StringVar()

# label section
question_label = Label(root, textvariable=question_text,bg="#25bcf7",font=("Times new roman", 15,"bold"))
question_label.config(wraplength=400,justify="center")
question_label.pack(pady=5)

option_label = Label(root, textvariable=option_text, font=("Times new roman", 14))
option_label.config(wraplength=400,justify="center",bg="#25bcf7")
option_label.pack()  # Adjust the y-coordinate as needed

# Entry for user's answer
answer_label=Label(root, text="Enter your Answer here: ",bg="#25bcf7",font=("Helvetica",12,'bold'))
answer_label.place(x=50,y=260)
answer_entry = Entry(root, font=("Times new roman", 14))
answer_entry.place(x=50,y=290)

# button Section
Start_Btn = tk.Button(root, text="Start", bg="#5478f0", font=("Verdana", 15, "bold", "italic"),command=lambda: start_quiz(selected_domain.get()))
Start_Btn.place(x=150, y=350)

Next_Btn = tk.Button(root, text="Next", bg="#07f0d5", font=("Verdana", 15, "bold", "italic"), command=next_question)
Next_Btn.place(x=360, y=350)

exit_Btn = tk.Button(root, text="Exit", bg="#f00755", font=("Verdana", 15, "bold", "italic"), command=root.destroy)
exit_Btn.place(x=260, y=350)

submit_Btn = tk.Button(root, text="Submit", bg="#555555", font=("Verdana", 15, "bold", "italic"), command=submit_answer, state=DISABLED)  # Initially disabled
submit_Btn.place(x=360, y=280)

root.mainloop()