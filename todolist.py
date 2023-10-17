tasks = []

while True:
    print("Options:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        task_num = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select a valid option.")
