version = "0.1.0"
status = "Development"

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
        print("Add Task Selected")
    elif choice == "2":
        print("View Tasks Selected")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")
      
