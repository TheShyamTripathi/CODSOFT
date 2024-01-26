# Importing all the required module
from tkinter import *

# Creating and initializing the tasks.txt file
with open("tasks.txt", "w"):
    pass

root = Tk()
root.title("My To-do List")
root.geometry("500x400")
root.resizable(0, 0)
root.config(bg="#755435")

# Heading Label
Label(root, text='My To Do List with Python', bg='#373730', fg='white', font=("Comic Sans MS", 20),
      pady=10).pack(fill='x')  

# Listbox with all the tasks with a scrollbar
tasks_listbox = Listbox(root, selectbackground="pink", bg='#f0f1f2', font=('Helvetica', 15),
                        height=10, width=25, borderwidth=0, highlightthickness=0)

scroller = Scrollbar(root, orient=VERTICAL, command=tasks_listbox.yview)
scroller.place(x=480, y=100, height=240)
tasks_listbox.place(x=220, y=100)
tasks_listbox.config(yscrollcommand=scroller.set)



# Adding items to the Listbox
with open('tasks.txt', 'r') as tasks_file:
    for task in tasks_file:
        tasks_listbox.insert(END, task.strip())

# Creating the Entry widget where the user can enter a new item
new_item_entry = Entry(root, width=23, font=('Helvetica', 12), bd=2, relief='groove')
new_item_entry.place(x=1, y=100)

# Creating the Buttons
add_btn = Button(root, text='Add Task', bg='Azure', fg="green", width=10, font=("Helvetica", 12),
                 command=lambda: add_item(new_item_entry, tasks_listbox))
add_btn.place(x=55, y=140)

edit_btn = Button(root, text='Edit Task', bg='#987433', fg="blue", width=10, font=("Helvetica", 12),
                  command=lambda: edit_item(new_item_entry, tasks_listbox))
edit_btn.place(x=55, y=190)

delete_btn = Button(root, text='Delete Task', bg='#931F2F', fg='white', width=10, font=('Helvetica', 12),
                    command=lambda: delete_item(tasks_listbox))
delete_btn.place(x=55, y=240)

# Adding and Deleting items functions
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()
    listbox.insert(END, new_task)

    with open('tasks.txt', 'a') as tasks_file:
        tasks_file.write(f'{new_task}\n')

def edit_item(entry: Entry, listbox: Listbox):
    selected_index = listbox.curselection()
    if selected_index:
        new_task = entry.get()
        listbox.delete(selected_index)
        listbox.insert(selected_index, new_task)

        with open('tasks.txt', 'r') as tasks_file:
            lines = tasks_file.readlines()

        with open('tasks.txt', 'w') as tasks_file:
            for i, line in enumerate(lines):
                if i != selected_index[0]:
                    tasks_file.write(line.strip() + '\n')

def delete_item(listbox: Listbox):
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

        with open('tasks.txt', 'r') as tasks_file:
            lines = tasks_file.readlines()

        with open('tasks.txt', 'w') as tasks_file:
            for i, line in enumerate(lines):
                if i != selected_index[0]:
                    tasks_file.write(line.strip() + '\n')

# Finalizing the window
root.update()
root.mainloop()
