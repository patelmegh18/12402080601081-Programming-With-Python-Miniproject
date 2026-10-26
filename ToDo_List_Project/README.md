# To-Do List Application (Console + GUI)

## Files
- `main.py` — original console application.
- `gui.py` — Tkinter GUI for adding, viewing, and deleting tasks.
- `tasks.txt` — saved tasks, one task per line.
- `README.md` — run instructions.

## Run the GUI
Open a terminal in this folder and run:

```bash
python gui.py
```

## Run the console version
```bash
python main.py
```

Python 3 is required. Tkinter is included with most standard Python installations.

## Task formatting fix
The GUI separates accidentally pasted literal `\n` sequences into individual tasks and rewrites the task file into the correct one-task-per-line format.
