#tasks ay yung array natin na pag lalagyan ng mga task, hindi ko alam ano pinaka effective na way pero I think tasks.append() yung gagamitin natin para mag delete
tasks = []

menu = input("""Hello user, whata do you wanna do?
                [A] Add a task
                [D] Delete a task
                [E] Edit a task
                Enter the letter: """)

#mga def natin
def addTasks():
    while True:
        add = input("Enter a task (press enter to stop): ")  #kailangan enter para ma input, pede mo ibahin to if u want
        if add.lower() == "":
            break
        else: 
            tasks.append(add)

    print("______THIS IS YOUR TASKS______")
    for add in tasks: #prints the tasks 
        
        print(add) #if kaya mo pre try mo lagyan ng number yung list natin like 1. 2. gamit ka loop idk din eh
        

  
#as of now di ko alam pano iloop program para makapag lagay ng multiple tasks... btw yung .lower() means tinatransform ko yung nakuhang string sa menu bilang lower case
if menu.lower() == 'a':
    addTasks()



















