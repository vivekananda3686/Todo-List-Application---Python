import tkinter as tk
from tkinter import messagebox, filedialog

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

def add_task():
    """Add a task to the list."""
    task = task_entry.get()
    if task:
        tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    """Remove the selected task from the list."""
    try:
        task_index = tasks.curselection()[0]
        tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def mark_task():
    """Mark the selected task as done."""
    try:
        task_index = tasks.curselection()[0]
        task = tasks.get(task_index)
        if " (Done)" not in task:
            tasks.delete(task_index)
            tasks.insert(tk.END, task + " (Done)")
        else:
            messagebox.showinfo("Info", "Task is already marked as done.")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")

def clear_tasks():
    """Clear all tasks from the list."""
    tasks.delete(0, tk.END)

def save_tasks():
    """Save the tasks to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks.get(0, tk.END):
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

def load_tasks():
    """Load tasks from a file."""
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        tasks.delete(0, tk.END)
        with open(file_path, "r") as file:
            for line in file:
                tasks.insert(tk.END, line.strip())
        messagebox.showinfo("Success", "Tasks loaded successfully!")

# Task list
tasks = tk.Listbox(root, width=50, height=15)
tasks.pack(pady=10)

# Task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

mark_button = tk.Button(button_frame, text="Mark as Done", command=mark_task)
mark_button.grid(row=0, column=2, padx=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks)
clear_button.grid(row=1, column=0, padx=5, pady=5)

save_button = tk.Button(button_frame, text="Save Tasks", command=save_tasks)
save_button.grid(row=1, column=1, padx=5, pady=5)

load_button = tk.Button(button_frame, text="Load Tasks", command=load_tasks)
load_button.grid(row=1, column=2, padx=5, pady=5)

# Start the main event loop
root.mainloop()
