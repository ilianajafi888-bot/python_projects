tasks = []


def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Delete task")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

    elif choice == "3":
        
        print("Delete not implemented yet.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
