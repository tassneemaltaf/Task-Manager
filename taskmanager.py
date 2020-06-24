# First we will go through the functions.
def listUsers():        # This function will help in printing the total number of users.
    user_file = open('user.txt', 'r')
    user_strings = user_file.readlines()
    return user_strings

def userNames():
    user_lines = listUsers()
    names = []

    for line in user_lines:
        line = line.split(", ")
        names.append(line[0])
    return names

def listTasks():        # This function will help in viewing the tasks assigned to a specific user and the total number of tasks.
    task_file = open('task.txt', 'r')
    task_strings = task_file.readlines()
    return task_strings


def reg_user(username):
    if username == "Admin":
        user_file = open('user.txt', 'a+')
        new_user = input("Enter your new username: ")

        names = userNames()
        if new_user in names:
            print("The username you have chosen already exists.")
            reg_user(username)
        else:
            new_pass = input("Enter your new password: ")
            user_file.write(new_user + ", " + new_pass + "\n")
            user_file.close()
    else:
        print("Only the user Admin is allowed to register users!")


def add_task():
    task_name = input("Enter the task name: ")
    usernew_name = input("Enter username: ")
    task_d = input("Enter task description: ")
    assign_date = input("Enter the date that the task was assigned to the user: ")
    date_due = input("Enter the due date for the task: ")
    task_comp = "No"
    new_task = task_name + ", " + usernew_name + ", " + task_d + ", " + assign_date + ", " + date_due + ", " + task_comp
    task_file = open('task.txt', 'a+')
    task_file.write(new_task + "\n")
    task_file.close()

def view_all():
    task_file = open('task.txt', 'r')
    for line in task_file:
        line = line.split(", ")
        print(f"""
Task: {line[0]}
Assigned to: {line[1]}
Task description: {line[2]}
Date assigned: {line[3]}
Due date: {line[4]}
Task complete: {line[5]}
""")
    task_file.close()


def view_mine(username):
    task_file = open('task.txt', 'r+')
    count = 0
    format_tasks = []
    user_tasks = []
    for task in task_file:
        format_tasks.append(task)
        task = task.split(", ")
        current_user = task[1]

        if username == current_user:
            count += 1
            current_task = f"""
                {count}.
                Task: 	{task[0]}
                Assigned to: 	{task[1]}
                Task description: 	{task[2]}
                Date assigned: 	{task[3]}
                Due date: 	{task[4]}
                Task Complete?:    {task[5]}   
                """
            user_tasks.append(current_task)
            print(current_task)
    task_file.close()

    select_opt = int(input("Select the task by typing its number or press -1 to return to the main menu: "))
    # Return to main menu option.
    if select_opt == "-1":
        menu(username)

    # Validation for out of bounds
    while select_opt > len(user_tasks) or select_opt < 1:
        select_opt = int(input("Incorrect. Select the task by typing its number or press -1 to return to the main menu: "))

    selected_task = format_tasks[select_opt - 1]
    print(selected_task)

    f = open('task.txt', 'r+')
    change = input("1.Mark as complete \n2.Edit\n")
    file_contents = []

    if change == "1":
        for line in f:
            line = line.split(", ")

            if line[1] == username:  # if the current task belongs to the user we want to target
                line[5] = "Yes"
                file_contents.append(", ".join(line).strip("\n"))
            else:
                file_contents.append(", ".join(line).strip("\n"))

        # Write the contents back to the file for the contents
        write_file = open('tasks.txt', 'w')
        print(file_contents)
        write_file.write("\n".join(file_contents))
        write_file.close()
    else:
        for line in f:
            line = line.split(", ")

            if line[1] == username:  # if the current task belongs to the user we want to target
                line[1] = input("Enter the new username: ")
                line[4] = input("Enter the new due date: ")
                file_contents.append(", ".join(line).strip("\n"))
            else:
                file_contents.append(", ".join(line).strip("\n"))

        # Write the contents back to the file for the contents
        edit_file = open('tasks.txt', 'w')
        print(file_contents)
        edit_file.write("\n".join(file_contents))
        edit_file.close()


def display_statistics():
    tasks = listTasks()
    users = listUsers()
    print("The total number of tasks: " + "\t" + str(len(tasks)))
    print("The total number of users: " + "\t" + str(len(users)))


def generate_reports():
    uofile = open('user_overview.txt', 'r')
    print("User Overview:\n")
    for line in uofile:
        print(line)
    uofile.close()

    tofile = open('task_overview.txt', 'r')
    print("Task Overview:\n")
    for line in tofile:
        print(line)
    tofile.close()


def menu(username):     # This is the menu function. It displays some information and asks the user to input a letter.
    print("Please select one of the following options: ")
    print("r - register user")
    print("a - add task")
    print("va - view all my tasks")
    print("vm - view my tasks")
    print("gr - generate reports")
    if username == "Admin":
        print("ds - display statistics")
    print("e - exit")
    menu_choice = input("")
    if menu_choice == "r":
        reg_user(username)

    elif menu_choice == "a":
        add_task()

    elif menu_choice == "va":
        view_all()

    elif menu_choice == "vm":
        view_mine(username)

    elif menu_choice == "gr":
        generate_reports()

    elif menu_choice == "ds":
        display_statistics()

    elif menu_choice == "e":
        quit()


def login_func():       # This one is the login function.
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user_file = open('user.txt', 'r')
    for line in user_file:
        line = line.split(", ")
        valid_user = line[0]
        valid_pass = line[1].strip("\n")
        if (username == valid_user) and (password == valid_pass):
            print("Welcome. You are logged in!")
            return menu(username)
    print("Invalid Username or password.Try again.")
    login_func()
login_func()
