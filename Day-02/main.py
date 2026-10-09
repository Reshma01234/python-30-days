version = "0.1.0"
status = "Development"

print("="*33)
print("     TASK MANAGER API")
print("="*33)
print(f"\nVersion: {version}")
print(f"\nStatus: {status}\n")
print("1. Add Task")
print("2. View Tasks")
print("3. Exit")

choice = int(input("Enter ypur choice:"))

if choice==1:
    print("Add Task Selected")
elif choice==2:
    print("View Tasks Selected")
elif choice==3:
    print("Goodbye")
else:
    print("Invalid Choice")
