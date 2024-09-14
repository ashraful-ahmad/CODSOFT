# to_do_manager.py

# Initialize lists to store tasks with days
task_list = []
day_list = []

# Function to add a task to the list
def insert_task(new_task):
    task_list.append(new_task)
    print(f"Task '{new_task}' successfully added.")

# Function to add a corresponding day for the task
def insert_day(assigned_day):
    day_list.append(assigned_day)
    print(f"Assigned Day '{assigned_day}' successfully added.")

# Function to remove a task and its day
def remove_task(task_index):
    if 0 <= task_index < len(task_list):
        deleted_task = task_list.pop(task_index)
        deleted_day = day_list.pop(task_index)  # Remove both task and day
        print(f"Task '{deleted_task}' and Day '{deleted_day}' removed.")
    else:
        print("Invalid task index. Try again.")

# Function to display all tasks along with their days
def display_tasks():
    if not task_list:
        print("No tasks available.")
    else:
        for i, (day, task) in enumerate(zip(day_list, task_list)):
            print(f"{i + 1}. Day: {day} | Task: {task}")

# Main function to handle the to-do list operations
def todo_menu():
    while True:
        print("\nTo-Do List Management Menu:")
        print("1. Add New Task")
        print("2. Remove Existing Task")
        print("3. View All Tasks")
        print("4. Exit")

        user_choice = input("Select an option (1-4): ")

        if user_choice == '1':
            task_input = input("Enter the task : ")
            day_input = input("Enter the day : ")
            task_input = task_input.capitalize()
            day_input = day_input.capitalize()
            insert_task(task_input)
            insert_day(day_input)

        elif user_choice == '2':
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")

        elif user_choice == '3':
            display_tasks()

        elif user_choice == '4':
            print("Exiting To-Do List Manager. Have a productive day!")
            break

        else:
            print("Invalid option. Please select from 1 to 4.")

# Entry point of the program
if __name__ == "__main__":
    todo_menu()
