import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry('400x400')
        self.root.config(bg='black')  
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="To-Do List", font=('Arial', 20, 'bold'), bg='black', fg='green')
        self.label.pack(fill=tk.X, pady=10)

        self.button_frame = tk.Frame(self.root, bg='black')
        self.button_frame.pack()

        self.add_button = tk.Button(self.button_frame, text="Add Task", font=('Arial', 14), bg='blue', fg='white', command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", font=('Arial', 14), bg='red', fg='white', command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.task_entry = tk.Entry(self.root, font=('Arial', 14))
        self.task_entry.pack(pady=5)

        self.tasks_frame = tk.Frame(self.root, bg='black')
        self.tasks_frame.pack(pady=10)

        self.task_list = tk.Listbox(self.tasks_frame, width=40, height=10, font=('Arial', 12), bg='green', fg='white', bd=0)
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.tasks_frame, orient=tk.VERTICAL, command=self.task_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_list.config(yscrollcommand=self.scrollbar.set)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
