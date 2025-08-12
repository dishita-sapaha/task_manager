import json
from task import Task
from datetime import datetime


class Storage:
    def __init__(self, filename='tasks.json'):
        self.filename = filename

    #saving our list of tasks IN json
    def save_tasks(self,tasks):
        data = []
        for task in tasks:
            data.append({
                "title" : task.title,
                "description": task.desc,
                "due_date": task.due_date,
                "completed": task.is_complete,
                "created_at": task.created_at.strftime("%Y-%m-%d %H:%M:%S")
            })
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)

    #loading our list of tasks FROM json
    def load_tasks(self):
        with open(self.filename, 'r') as f:
            try:
                data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                return []
        
        tasks = []
        for item in data:
            created = datetime.strptime(item['created_at'], "%Y-%m-%d %H:%M:%S") 
            t = Task(item['title'], item['description'], item['due_date'])
            t.is_complete = item['completed']
            t.created_at = created
            tasks.append(t)

        return tasks



        
