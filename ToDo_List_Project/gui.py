"""
To-Do List GUI
Uses the load_tasks() and save_tasks() functions from main.py.
Run with: python gui.py
"""

import tkinter as tk
from tkinter import messagebox
from main import load_tasks, save_tasks


def clean_task_list(raw_tasks):
    """Convert accidental literal \\n sequences into separate task lines."""
    cleaned = []
    for raw_task in raw_tasks:
        # If the user pasted text containing the two characters backslash+n,
        # interpret those as line breaks and make each line its own task.
        normalized = raw_task.replace("\\r\\n", "\n").replace("\\n", "\n").replace("\\r", "\n")
        cleaned.extend(line.strip() for line in normalized.splitlines() if line.strip())
    return cleaned


class ToDoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("520x560")
        self.root.minsize(420, 440)
        self.root.configure(bg="#f2f5fb")

        self.tasks = clean_task_list(load_tasks())
        save_tasks(self.tasks)  # Rewrite old malformed entries in the correct format.

        header = tk.Frame(root, bg="#263b63", padx=20, pady=18)
        header.pack(fill="x")
        tk.Label(
            header, text="TO-DO LIST APPLICATION",
            font=("Arial", 18, "bold"), bg="#263b63", fg="white"
        ).pack(anchor="w")
        tk.Label(
            header, text="Keep track of your daily tasks",
            font=("Arial", 10), bg="#263b63", fg="#dbe6ff"
        ).pack(anchor="w", pady=(5, 0))

        body = tk.Frame(root, bg="#f2f5fb", padx=20, pady=18)
        body.pack(fill="both", expand=True)

        tk.Label(
            body, text="Enter a task:", font=("Arial", 11, "bold"),
            bg="#f2f5fb", fg="#263b63"
        ).pack(anchor="w")

        entry_row = tk.Frame(body, bg="#f2f5fb")
        entry_row.pack(fill="x", pady=(7, 14))

        self.task_entry = tk.Entry(entry_row, font=("Arial", 11), relief="solid", bd=1)
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=7, padx=(0, 8))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        tk.Button(
            entry_row, text="Add Task", command=self.add_task,
            bg="#2f6fed", fg="white", relief="flat",
            padx=12, pady=7, cursor="hand2"
        ).pack(side="right")

        tk.Label(
            body, text="Your tasks:", font=("Arial", 11, "bold"),
            bg="#f2f5fb", fg="#263b63"
        ).pack(anchor="w", pady=(0, 7))

        list_frame = tk.Frame(body, bg="white", bd=1, relief="solid")
        list_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_list = tk.Listbox(
            list_frame, font=("Arial", 11), bg="white", fg="#24324a",
            selectbackground="#cfe0ff", activestyle="none",
            bd=0, highlightthickness=0, yscrollcommand=scrollbar.set
        )
        self.task_list.pack(side="left", fill="both", expand=True, padx=8, pady=8)
        scrollbar.config(command=self.task_list.yview)

        buttons = tk.Frame(body, bg="#f2f5fb")
        buttons.pack(fill="x", pady=(12, 6))

        tk.Button(
            buttons, text="Delete Selected", command=self.delete_task,
            bg="#d94b4b", fg="white", relief="flat",
            padx=12, pady=8, cursor="hand2"
        ).pack(side="left")

        tk.Button(
            buttons, text="Refresh", command=self.refresh_tasks,
            bg="#e1e8f4", fg="#263b63", relief="flat",
            padx=14, pady=8, cursor="hand2"
        ).pack(side="right")

        self.count_label = tk.Label(
            body, text="", font=("Arial", 9),
            bg="#f2f5fb", fg="#5a6880"
        )
        self.count_label.pack(anchor="w", pady=(4, 0))

        self.refresh_tasks()
        self.task_entry.focus_set()

    def add_task(self):
        raw_text = self.task_entry.get().strip()
        if not raw_text:
            messagebox.showwarning("Empty Task", "Task cannot be empty.")
            return

        # Split pasted entries like "Study\\nRead" into separate tasks.
        normalized = raw_text.replace("\\r\\n", "\n").replace("\\n", "\n").replace("\\r", "\n")
        new_tasks = [line.strip() for line in normalized.splitlines() if line.strip()]
        if not new_tasks:
            messagebox.showwarning("Empty Task", "Task cannot be empty.")
            return

        self.tasks.extend(new_tasks)
        save_tasks(self.tasks)
        self.task_entry.delete(0, tk.END)
        self.refresh_tasks()

        if len(new_tasks) == 1:
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showinfo("Success", f"{len(new_tasks)} tasks added separately.")

    def delete_task(self):
        selection = self.task_list.curselection()
        if not selection:
            messagebox.showinfo("Select Task", "Please select a task to delete.")
            return

        index = selection[0]
        task = self.tasks[index]
        if messagebox.askyesno("Confirm Delete", f"Delete this task?\n\n{task}"):
            self.tasks.pop(index)
            save_tasks(self.tasks)
            self.refresh_tasks()

    def refresh_tasks(self):
        self.tasks = clean_task_list(load_tasks())
        save_tasks(self.tasks)
        self.task_list.delete(0, tk.END)

        for number, task in enumerate(self.tasks, start=1):
            self.task_list.insert(tk.END, f"{number}. {task}")

        self.count_label.config(text=f"Total tasks: {len(self.tasks)}")


if __name__ == "__main__":
    window = tk.Tk()
    app = ToDoGUI(window)
    window.mainloop()
