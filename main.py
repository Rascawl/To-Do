
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

def editTask():

    while True:
        file_path = input("Please enter the file name of the task you want to edit: ")
        try:
            with open(file_path, "r") as file:
                editList = file.readlines()
            print("".join(editList))
            break

        except FileNotFoundError:
            print("List does not exist")
        
    while True:
        try:
            index = int(input("Select the number of task you want to edit: "))
            
            if index <= 0 or index >= len(editList):
                print("Task out of bounds, try again")
                continue

            newTask = input("Enter a new task: ")

            editList[index] = f"{index}. {newTask}\n"
        except ValueError:
            print("Error try again")

        with open(file_path, "w") as file:
            file.writelines(editList)

        print("Task updated succesfully")
        break

def createTasks():

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

def addTasks():
    
    while True:
        file_path = input("Please enter the file name of the task you want to edit: ")
        try:
            with open(file_path, "r") as file:
                editList = file.readlines()
            print("".join(editList))
            break

        except FileNotFoundError:
            print("List does not exist")
    
    currentNumber = len(editList) - 1

    with open(file_path, "a") as file:
        while True:
            addTask = input("Enter new Task (press enter to stop): ")
            if addTask == "":
                break
            currentNumber +=1
            file.write(f"{currentNumber}. {addTask}\n")
        print("Tasks added succesfully")

menu = input("""Hello user, whata do you wanna do?
                [C] Create new List
                [A] Add a task
                [D] Delete a task
                [E] Edit a task
                Enter the letter: """)

if menu.lower() == 'c':
    createTasks()
elif menu.lower() == 'e':
    editTask()
elif menu.lower() == 'a':
    addTasks()
    