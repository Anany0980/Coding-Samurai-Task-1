# to-do list application

tasks = []

def add_task(title, description):
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)

def list_tasks():
    for task in tasks:
        print(f"{task['title']}: {task['description']}")

def mark_task_complete(task_id):
    task = tasks[task_id]
    task["completed"] = True

def delete_task(task_id):
    tasks.pop(task_id)

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['title']},{task['description']},{task['completed']}\n")

def load_tasks():
    with open("tasks.txt", "r") as f:
        for line in f:
            task = line.split(",")
            tasks.append({"title": task[0], "description": task[1], "completed": task[2]})

def main():
    load_tasks()

    while True:
        print("To-Do List Application")
        print("1. Add a task")
        print("2. List tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Save tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the task: ")
            description = input("Enter the description of the task: ")
            print()
            add_task(title, description)
        elif choice == "2":
            list_tasks()
            print()
        elif choice == "3":
            task_id = int(input("Enter the ID of the task to mark as complete: "))
            print()
            mark_task_complete(task_id)
        elif choice == "4":
            task_id = int(input("Enter the ID of the task to delete: "))
            print()
            delete_task(task_id)
        elif choice == "5":
            save_tasks()
            print()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == "__main__":
    main()