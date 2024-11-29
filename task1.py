import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.root.title("To-Do List")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="To-Do List", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Add Task
        tk.Label(self.root, text="Task:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.task_entry = tk.Entry(self.root, width=40)
        self.task_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=1, column=2, padx=5, pady=5)

        # Task List
        self.task_list = tk.Text(self.root, width=50, height=10, state=tk.DISABLED)
        self.task_list.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Update and Delete
        tk.Label(self.root, text="Task Number:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.task_number_entry = tk.Entry(self.root, width=5)
        self.task_number_entry.grid(row=3, column=1, sticky="w", padx=5)

        tk.Button(self.root, text="Update Task", command=self.update_task).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Delete Task", command=self.delete_task).grid(row=4, column=1, padx=5, pady=5)

    def refresh_task_list(self):
        """Refresh the task list display."""
        self.task_list.config(state=tk.NORMAL)
        self.task_list.delete(1.0, tk.END)
        if not self.tasks:
            self.task_list.insert(tk.END, "No tasks available.\n")
        else:
            for i, task in enumerate(self.tasks, start=1):
                self.task_list.insert(tk.END, f"{i}. {task}\n")
        self.task_list.config(state=tk.DISABLED)

    def add_task(self):
        """Add a new task."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            messagebox.showinfo("Success", f"Task '{task}' added.")
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showerror("Error", "Task cannot be empty.")

    def update_task(self):
        """Update an existing task."""
        try:
            index = int(self.task_number_entry.get().strip()) - 1
            new_task = self.task_entry.get().strip()
            if new_task and 0 <= index < len(self.tasks):
                old_task = self.tasks[index]
                self.tasks[index] = new_task
                messagebox.showinfo("Success", f"Task '{old_task}' updated to '{new_task}'.")
                self.task_entry.delete(0, tk.END)
                self.task_number_entry.delete(0, tk.END)
                self.refresh_task_list()
            else:
                messagebox.showerror("Error", "Invalid task number or empty new task.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Enter a valid task number.")

    def delete_task(self):
        """Delete a task."""
        try:
            index = int(self.task_number_entry.get().strip()) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                messagebox.showinfo("Success", f"Task '{removed_task}' deleted.")
                self.task_number_entry.delete(0, tk.END)
                self.refresh_task_list()
            else:
                messagebox.showerror("Error", "Invalid task number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Enter a valid task number.")

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop()
