# Todo List App Using OOP
from datetime import datetime

# Task class to hold individual task details
class Task:
    def __init__(self, title, priority, deadline):
        self.title = title
        self.priority = priority
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.completed = False
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} | Priority: {self.priority} | Deadline: {self.deadline.date()} | Status: {status}"


# TodoList class to manage a list of tasks
class Todolist:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, priority, deadline):
        task = Task(title, priority, deadline)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.\n")

    def show_tasks(self):
        if not self.tasks:
            print("No Tasks in the list.\n")
            return

        # sort by priority and deadline
        sorted_tasks = sorted(self.tasks, key=lambda x: (x.priority, x.deadline))
        for idx, task in enumerate(sorted_tasks, 1):
            print(f"{idx}. {task}")
        print()
    
    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Task '{self.tasks[index].title}' marked as completed.\n")
        else:
            print("Invalid task number.\n")
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Task '{removed.title}' removed.\n")
        else:
            print("Invalid task number.\n")


# Main logic
def run_app():
    todo = Todolist()
    print("Welcome to Python ToDo List with Priority and Deadlines.\n")

    while True:
        print("Options:")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input("Task Title: ")
            priority = input("Priority (High/Medium/Low): ").capitalize()
            deadline = input("Deadline (YYYY-MM-DD): ")
            todo.add_task(title, priority, deadline)

        elif choice == '2':
            todo.show_tasks()

        elif choice == '3':
            index = int(input("Enter task number to mark as complete: ")) - 1
            todo.mark_task_done(index)

        elif choice == '4':
            index = int(input("Enter task number to remove: ")) - 1
            todo.remove_task(index)

        elif choice == '5':
            print("Exiting the app. Have a productive day!")
            break

        else:
            print("Invalid choice. Try again.\n")


# Run the app
if __name__ == "__main__":
    run_app()
