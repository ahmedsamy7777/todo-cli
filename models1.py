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
        self.tasks = []

    def SetTask(self, name):
        self.tasks.append(Task(name))

    def checkAtask(self, task_no):
        if 1 <= task_no <= len(self.tasks):
            self.tasks[task_no - 1].isdone = True
        else:
            print("task not found")

    def delete_task(self, task_no):
        if 1 <= task_no <= len(self.tasks):
            self.tasks.pop(task_no - 1)
        else:
            print("task not found")

    def ShowTasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"Task {i}: {task.name}")
            print(f"Date: {task.date}")
            print("checked" if task.isdone else "Not checked")
            print("___________________________________")

    def save(self, tasks_rebo="tasks.json"):
        data = [task.to_dict() for task in self.tasks]
        with open(tasks_rebo, "w") as f:
            json.dump(data, f)

    def load(self, tasks_rebo="tasks.json"):
        try:
            with open(tasks_rebo, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            print("task")
            return
        self.tasks = [Task.from_dict(d) for d in data]