from manager import TaskManager

def main():
    tm = TaskManager()

    while True:
        print("\n==== Task Manager ====")
        print("1. Add task")
        print("2. Remove task")
        print("3. Complete task")
        print("4. List tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description (optional): ")
            due = input("Due date (optional, format YYYY-MM-DD): ")
            tm.add_task(title, desc, due if due else None)

        elif choice == "2":
            title = input("Enter title of task to remove: ")
            tm.remove_task(title)

        elif choice == "3":
            title = input("Enter title of task to mark complete: ")
            tm.complete_task(title)

        elif choice == "4":
            tm.list_tasks()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
