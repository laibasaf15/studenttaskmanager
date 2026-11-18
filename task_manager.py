
tasks = []


def add_task(title):
    if not title.strip():
        return False

    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "completed": False
    }

    tasks.append(task)
    return True


def display_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Student Tasks ---")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"

        print(
            f'ID: {task["id"]} | '
            f'Title: {task["title"]} | '
            f'Status: {status}'
        )


def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            if add_task(title):
                print("Task added successfully!")
            else:
                print("Task title cannot be empty!")

        
        elif choice == "2":
            display_tasks()

        elif choice == "3":
            print("Exiting Student Task Manager. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
