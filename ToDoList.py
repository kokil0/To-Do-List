todo_tasks = []

def addTask(task_name):
    task = {"task": task_name, "completed": False}
    todo_tasks.append(task)
    print(f"Task '{task_name}' added to your to-do list.")

def markCompleted(task):
    if 1 <= task <= len(todo_tasks):
        todo_tasks[task - 1]["completed"] = True
        print(f"Task {task} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

def removeTask(task):
    if 1 <= task <= len(todo_tasks):
        removed_task = todo_tasks.pop(task - 1)
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

while True:
    print("\nOptions:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        if not todo_tasks:
            print("Your to-do list is empty.")
        else:
            print("To-Do List:")
            for i, task in enumerate(todo_tasks, start=1):
                status = "Done" if task["completed"] else "Not Done"
                print(f"{i}. {task['task']} ({status})")

    elif choice == '2':
        task_name = input("Enter the task: ")
        addTask(task_name)

    elif choice == '3':
        task = int(input("Enter the task number to mark as completed: "))
        markCompleted(task)

    elif choice == '4':
        task = int(input("Enter the task number to remove: "))
        removeTask(task)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Please enter a valid option.")
