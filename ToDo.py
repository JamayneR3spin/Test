class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False
#when this function is called upon it will change the status from false to true.
    def mark_complete(self):
        self.is_completed = True
#The most important function, this will be where I create a task name and include it in the list
def add_task(todo_list):
    description = input("Enter the task here: ")
    new_task = Task(description)
    todo_list.append(new_task)
    print(f"Task '{description}' is now added to the list.")

#This function will first check if the list is empty,
def view_tasks(todo_list):
    if not todo_list:
        print("Your list is currently empty.")
        return
    print("\n--- Your To-Do List ---")
    for index, task in enumerate(todo_list):
        status = "[X]" if task.is_completed else "[ ]"
        print(f"{index + 1}. {status} {task.description}")
        print("---\n")
#This handles where the task is marked as completed. Changing the is_complete from the default FALSE to TRUE
def mark_task_as_completed(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return
    #Something i want to keep looking into as error handling is something that will be crucial and i will apply this to my quiz
    try:
        task_index = int(input("Enter the task number to mark as complete: "))
        task_description = todo_list[task_index-1].description
        if 1<= task_index <= len(todo_list):
            todo_list[task_index-1].mark_complete()
            print(f"Task '{task_description}' marked as complete.")
        else:
            print("Invalid task number.")
            #This is for error handling, so it will display the below message without breaking the code
    except ValueError:
        print("Invalid input. Please enter a number.")
   #This is where all my tasks are stored
my_todo_list = []

#Main part of code, this will be what the user is displayed with upon entry
while True:
    print("\n --- To Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")
#This is where the user input directs you to different functions, using the list as its base point.
#Maybe add a 5th choice to uncheck a task complete and potentially a 6th choice to clear completed tasks from the list.
    if choice == '1':
        add_task(my_todo_list)
    elif choice == '2':
        view_tasks(my_todo_list)
    elif choice == '3':
        mark_task_as_completed(my_todo_list)
    elif choice == '4':
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")