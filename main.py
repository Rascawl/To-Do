#task ay yung array natin na pag lalagyan ng mga task, hindi ko alam ano pinaka effective na way pero I think tasks.append() yung gagamitin natin para mag delete
task = []

#Ito menu natin gamit tayo def(), pero isip kapa din if may mas effective way mag handle ng options
menu = input("""Hello user, what do you wanna do?
                [A] Add a task
                [D] Delete a task
                [E] Edit a task
                Enter the letter: """)
def addTasks():
    add = input("Enter a task: ") 
    task.append(add)

    print("Here is your pending task: \n", ", ".join(task))
 

#as of now di ko alam pano iloop program para makapag lagay ng multiple tasks... btw yung .lower() means tinatransform ko yung nakuhang string sa menu bilang lower case
if menu.lower() == 'a':
    addTasks()


















