from tkinter import *
from tkinter import messagebox
import random 
import string

def generatePassword():
    global length_entry
    length_value = length_entry.get()
    if length_value.isdigit():
        length = int(length_value)
    else:
        length_entry.config(state='normal')
        length_entry.delete(0, 'end')
        length_entry.insert(0, "Integer only")
        length_entry.config(state='normal')
        return None

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function Section
def passwordGenerate(op):
    global operator
    operator = op
    user_id = name_entry.get()
    if operator == "G":
        result_entry.delete(0, 'end')
        if not user_id or not length_entry.get():
            result_entry.config(state='normal')
            result_entry.delete(0, 'end')
            result_entry.insert(0, "Please fill above.")
            result_entry.config(state='readonly')
        else:
            generated_password = generatePassword()
            if generated_password:
                result_entry.config(state='normal')
                result_entry.delete(0, 'end')
                result_entry.insert(0, generated_password)
                result_entry.config(state='readonly')
    elif operator == "A":
        password_checker = result_entry.get()
        if not user_id or not length_entry.get() or not password_checker:
            result_entry.config(state='normal')
            result_entry.delete(0, 'end')
            result_entry.insert(0, "password not generated")
            result_entry.config(state='readonly')
        else:
            messagebox.showinfo('Successful', "Thanks, you successfully generated a password")
    else:
        messagebox.showinfo("Exit", "Thank You, visit again")

root = Tk()
root.geometry("400x320")
root.config(bg="#f8008f")
root.title("Random Password Generator")
root.iconbitmap("key_password_lock_800.ico")
root.resizable(0, 0)

# Title
text_label = Label(root, text="Password Generator", bg="#f8008f", fg="#0055ff")
text_label.config(font=("Times New Roman", 25, "bold", "italic", "underline"))
text_label.pack(pady=(2, 5))

# Entry for user name
name_label = Label(root, text="Enter user ID:", bg="#f8008f", fg="#0000ff")
name_label.config(font=("Times New Roman", 10, "bold", "italic"))
name_label.place(x=15, y=80)

name_entry = Entry(root, width=20, font=("times new roman", 12), bg="#d8008d")
name_entry.place(x=165, y=80)

# Entry for password length
length_label = Label(root, text="Enter Password Length:", bg="#f8008f", fg="#0000ff")
length_label.config(font=("Times New Roman", 10, "bold", "italic"))
length_label.place(x=15, y=130)

length_entry = Entry(root, width=20, font=("times new roman", 12), bg="#d8008d")
length_entry.place(x=165, y=130)

# Generated password display
password_label = Label(root, text="Generated Password:", bg="#f8008f", fg="#0000ff")
password_label.config(font=("Times New Roman", 10, "bold", "italic"))
password_label.place(x=15, y=180)

result_entry = Entry(root, width=20, font=("times new roman", 12), bg="#d8008d")
result_entry.place(x=165, y=180)

# Button Section
generate_button = Button(root, text="Generate", bg="#888888", fg="aqua", command=lambda: passwordGenerate("G"))
generate_button.config(font=("verdana", 15, "bold"), height=1)
generate_button.place(x=20, y=250)

accept_button = Button(root, text="Accept", bg="#555555", fg="aqua", command=lambda: passwordGenerate("A"))
accept_button.config(font=("verdana", 15, "bold"), height=1)
accept_button.place(x=160, y=250)

reject_button = Button(root, text="Reject", bg="tomato", fg="aqua", command=lambda: passwordGenerate("R"))
reject_button.config(font=("verdana", 15, "bold"), height=1)
reject_button.place(x=280, y=250)

root.mainloop()
