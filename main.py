from models1 import Task, ToDoList
tdl= ToDoList()
tdl.load()




while(True):
    print("\nn: New task | c: Check a task | s: Show tasks | e: Exit")
    flag =  input("Up to what?: ")
    if flag == 'n':
        name = input("Enter the task name:")
        tdl.SetTask(name)
    elif flag == 'c':
      try : 
          num = int (input("task number: "))
      except: print("please enter a number!")
      tdl.checkAtask(num)

    elif flag == 's':
        tdl.ShowTasks()
    elif flag == 'e':
      
        break    
    else: print("Choose a flag from list please!")
    tdl.save() 




