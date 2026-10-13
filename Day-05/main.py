version = "0.1.0"
status = "Development"


def display_task_manager_menu():
    print("=" * 33)
    print("         TASK MANAGER")
    print("=" * 33)
    print(f"\nVersion: {version}")
    print(f"Status: {status}\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-3): ").strip()

        if not choice:
            print("Choice cannot be empty. Please enter 1, 2, or 3.")
        elif choice in ("1", "2", "3"):
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def get_task_description():
    while True:
        task_description = input("Enter task description: ").strip()

        if not task_description:
            print("Task description cannot be empty. Please try again.")
            continue

        return task_description


def add_task(tasks):
    task_description = get_task_description()

    if task_description in tasks:
        print("This task already exists.")
        return

    tasks.append(task_description)
    print("Task added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for task_number, task_description in enumerate(tasks, start=1):
        print(f"{task_number}. {task_description}")


def main():
    tasks = []

    while True:
        display_task_manager_menu()
        choice = get_menu_choice()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
