
#tasks ay yung array natin na pag lalagyan ng mga task, hindi ko alam ano pinaka effective na way pero I think tasks.append() yung gagamitin natin para mag delete
tasks = []

def saveTask():
    file_path = input("Please enter the file name of your task: ")
    try:
        with open(file_path, "x") as file:
            file.write("______THIS IS YOUR TASKS______\n")
            for i, task in enumerate(tasks, start=1):
                file.write(f"{i}. {task}\n")
        print("Tasks saved")
    except FileExistsError:
        print("There is a list with the same name")

def readTask():
    file_path = input("Please enter the file name of the task you want to edit: ")
    with open(file_path, "r") as file:
        contentList = file.read()
        print(contentList)


def addTasks():
    while True:
        add = input("Enter a task (press enter to stop): ")  
        if add.lower() == "":
            break
        else: 
            tasks.append(add)
            
    print("______THIS IS YOUR TASKS______")
    for i, add in enumerate(tasks, start =1):
        print(f"{i}. {add}")

    confirm = input("Do you want to save? Y/N: ")
    if confirm.lower() == 'y':
        saveTask()

menu = input("""Hello user, whata do you wanna do?
                [A] Add a task
                [D] Delete a task
                [E] Edit a task
                Enter the letter: """)

if menu.lower() == 'a':
    addTasks()
elif menu.lower() == 'e':
    readTask()
    



















