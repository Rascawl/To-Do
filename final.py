
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

def addTask():

    
    while True:
        add = input("Enter a task (press enter to stop): ")  
        if add.lower() == "":
            break
        else: 
            tasks.append(add)
            
    viewTask()
    
def viewTask():

    print("\n")
    print("______THIS IS YOUR TASKS______")
    for i, add in enumerate(tasks, start =1):
        print(f"{i}. {add}")
    
    print("\n")

def deleteTask():

    viewTask()
    while True:
        index = int(input("Please enter the number you want to delete: "))
        print("\n")
        index -= 1
        
        if index <= 0 or index >= len(tasks):
            print("Task out of bounds, try again")
        else:
            break

    tasks.pop(index)
    print("Succesfully deleted")

def markDone():
    while True:
        file_path = input("Please enter the name of file: ")
        try:
            with open(file_path, "r") as file:
                markList = file.readlines()
            print("".join(markList))
            break

        except FileNotFoundError:
            print("List does not exist")
    while True:
        index = int(input("Enter the number of task you want to mark as done: "))
        if 1 <= index <= len(markList):
        
            markList[index] = markList[index].rstrip("\n") + " --X\n"
            break
        else:
            print("Task out of bounds")

    with open(file_path, "w") as file:
        file.writelines(markList)

    print("Task marked as done!")


def menu():
    while True:
        option = input("""Hello user, what do you wanna do?
                        [S] Save task
                        [V] View tasks
                        [A] Add a task
                        [D] Delete a task
                        [M] Mark a task as done
                        [X] Exit Program
                        Enter the letter: """).lower()
        match option:
            case "s":
                saveTask()
            case "v":
                viewTask()
            case "a":
                addTask()
            case "d":
                if not tasks:
                    print("There are no tasks")
                else:
                    deleteTask()
            case "m":
                markDone()
            case "x":
                print("Program closed")
                quit()

menu()





 
      
    