from datetime import date
import json
from tabnanny import check
class Task:
            def __init__(self, name, due_date = None, state = False):
                self.name= name
                self.date=  due_date or date.today().isoformat()
                self.isdone = state
            def to_dict(self):
                return {
                   "name": self.name,
                   "date": self.date,
                   "state": self.isdone
                 }
            def from_dict(d):
                return Task(d["name"] , d["date"], d["state"])

class ToDoList:
     
   
   
   def __init__(self):
       self.TaskCount = 0
     
       self.task_rebo = dict()


   def SetTask(self, name):
        self.TaskCount +=1 
        self.task_rebo[f"Task {self.TaskCount}"] = Task(name)
   def checkAtask(self, task_no):
    key = f"Task {task_no}"
    if key in self.task_rebo:
        self.task_rebo[key].isdone = True
    else:
        print("task not found")
   
   def descirbe(self):
        pass
   def ShowTasks(self):
      for key, task in self.task_rebo.items(): 
        print(self.TaskCount)
        print(f"{key}: {task.name} ")  
        print(f"Date:{task.date}")
        if task.isdone == False:
            print ("Not checked")
        else: print("checked")
        print("___________________________________")
   def save(self):
       with open("tasks_rebo", 'w') as f:
            t = [task.to_dict()for task in self.task_rebo.values()]
            json.dump(t, f)

   def load(self):
      try:
          with open("tasks_rebo", 'r') as f:
           tasks = json.load(f)
        
      
      except json.JSONDecodeError:
          return
      for t in tasks : 
        self.TaskCount += 1
        self.task_rebo[f"Task {self.TaskCount}"] = Task.from_dict(t)

