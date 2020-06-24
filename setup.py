# The program was created using two python files: setup.py and taskmanager.py.
# setup.py contains the text files and taskmanager.py contains all the functions.
# First you need to run setup.py and then taskmanager.py.

from datetime import datetime   # Importing a module that we will use later.

user_file = open('user.txt', 'w+')      # Creating user.txt text file.

# First we need to create the username and password variables.
user_names = "Admin, Username1, Username2, Username3"
pass_words = "Adm1n, Incorrect1, John12, Password0"

user_list = user_names.split(", ")      # Splitting the users and passwords.
pass_list = pass_words.split(", ")
correspond_user = list(zip(user_list, pass_list))   # Combining every password with its respective username.
for user in correspond_user:
    user_file.write(str(", ".join(user) + "\n"))    # Writing it in the text file.
user_file.close()

task_file = open('task.txt', 'w+')      # Creating task.txt.

tasks = "Assign initial tasks, Register users, Print documents, Open new bank account."
task_description = "Use taskManager.py to add the users and pass, Use taskManager.py to assign task to each member, Use printer, Go to bank "
date_assign = "10 Jan 2020, 25 Jan 2020, 1 Feb 2020, 9 Feb 2020"
due_date = "15 Mar 2020, 30 Mar 2019, 10 Apr 2020, 3 May 2020"
complete_task = "Yes, No, No, Yes"

task_split = tasks.split(", ")      # Splitting every single string.
taskd_split = task_description.split(", ")
date_split = date_assign.split(", ")
due_split = due_date.split(", ")
complete_split = complete_task.split(", ")
correspond_task = list(zip(task_split, user_list, taskd_split, date_split, due_split, complete_split))
# And corresponding each task to its user.

for task in correspond_task:
    task_file.write(str(", ".join(task) + "\n"))
task_file.close()

# Creating the task_overview.txt file
tofile = open('task_overview.txt', 'w+')
task_file = open('task.txt', 'r')
task_read = task_file.readlines()
total_tasks = len(task_read)

tofile.write("The total number of tasks that have been generated and tracked using task_manager.py: " + str(total_tasks))

completed_tasks = 0
incompleted_tasks = 0
incompleted_overdue = 0
for line in task_read:
    line = line.strip("\n").split(", ")
    # print(line[5])
    if line[5] == "Yes":
        completed_tasks += 1
    else:  # Incomplete
        incompleted_tasks += 1

        # Do test for overdue
        due_date = line[4]
        current_date = datetime.now()

        due_date = datetime.strptime(due_date, "%d %b %Y")

        # current_date = datetime.strptime(current_date, "%d %b %Y")
        if due_date < current_date:
            incompleted_overdue += 1

        print(due_date)

tofile.write(f"\nCompleted tasks: {completed_tasks}")
tofile.write(f"\nIncompleted tasks: {incompleted_tasks}")
tofile.write(f"\nIncompleted and overdue: {incompleted_overdue}")
tofile.write(f"\nThe percentage of incomplete tasks: {incompleted_tasks / total_tasks * 100:.2f}%")
tofile.write(f"\nThe percentage of incomplete tasks: {incompleted_overdue / total_tasks * 100:.2f}%\n")

tofile.close()

# Now we will work on the user_overview.txt file.
uofile = open('user_overview.txt', 'w+')
user_file = open('user.txt', 'r')
user_read = user_file.readlines()
total_users = len(user_read)

uofile.write(f"The total number of users that have been generated and tracked using task_manager.py: {total_users}")
uofile.write(f"\nThe total number of tasks that have been generated and tracked using task_manager.py: {total_tasks}")

task_file = open('tasks.txt', 'r')
line_read = task_file.readlines()

total_user = 0
completed_user = 0
incompleted_user = 0
user_overdue = 0
username = input("Enter your username: ")

for line in line_read:
    line_split = line.strip("\n").split(", ")
    if line_split[1] == username:
        total_user += 1
        if line_split[5] == "Yes":
            completed_user += 1
        else:
            incompleted_user += 1

            due_user = line[4]
            current_date = datetime.now()

            due_user = datetime.strptime(due_user, "%d %b %Y")

            if due_user < current_date:
                user_overdue += 1

                due_user = line_split[4]
                today_date = datetime.now()

                due_user = datetime.strptime(due_user, "%d %b %Y")

                if due_user < today_date:
                    user_overdue += 1
    else:
        pass

uofile.write(f"\nThe total number of tasks assigned to your user: {total_user}")
uofile.write(f"\nThe percentage of the total number of tasks assigned to your user: {total_user / total_tasks * 100:.2f}%")
if completed_user > 0:
    uofile.write(f"\nThe percentage of tasks assigned to your user that have been completed: {completed_user / total_user * 100:.2f}%")
else:
    uofile.write(
        f"\nThe percentage of tasks assigned to your user that have been completed: 0")
if incompleted_user > 0:
    uofile.write(f"\nThe percentage of tasks assigned to your user that must still be completed: {incompleted_user / total_user * 100:.2f}%")
else:
    uofile.write(f"\nThe percentage of tasks assigned to your user that must still be completed: 0%")
if user_overdue > 0:
    uofile.write(f"\nThe percentage of tasks assigned to your user that must still be completed and are overdue: {user_overdue / total_user * 100:.2f}%")
else:
    uofile.write(f"\nThe percentage of tasks assigned to your user that must still be completed and are overdue: 0%\n")


task_file.close()
uofile.close()