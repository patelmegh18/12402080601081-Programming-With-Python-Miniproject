def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def add_task(tasks):
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")


def delete_task(tasks):
    view_tasks(tasks)

    if tasks:
        try:
            number = int(input("Enter task number to delete: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST APPLICATION ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Thank you for using the application.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
