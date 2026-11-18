
tasks = []


def add_task(title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


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

def complete_task(task_id):
    for task in tasks:
       if task["id"] == task_id:
        if task["completed"]:
            return False
        task["completed"] = True
        return True

    return False


def main():
    while True:
        print("\n===== Student Task Manager =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Complete Task")
        print("4. Exit")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)

        elif choice == "2":
            display_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
                if complete_task(task_id):
                    print("Task marked as completed!")
            except ValueError:
                print("Please enter a valid numeric task ID.")
            except ValueError:
                print("Please enter a valid numeric task ID.")
        elif choice == "4":
            print("Exiting Student Task Manager. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
