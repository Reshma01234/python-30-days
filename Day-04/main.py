version = "0.1.0"
status = "Development"
tasks = []

while True:
    print("=" * 33)
    print("         TASK MANAGER")
    print("=" * 33)
    print(f"\nVersion: {version}")
    print(f"\nStatus: {status}\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task = input("Enter task: ").strip()

        if not task:
            print("Task description cannot be empty.")
        else:
            tasks.append(task)
            print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        print("Goodbye")
        break

    else:
        print("Invalid Choice")
      
