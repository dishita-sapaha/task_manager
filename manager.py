from task import Task
from storage import Storage

#create a class for managing tasks which includes methods like add(), remove(), complete(), find() and show() tasks
class TaskManager:
    def __init__(self):
        self.storage = Storage()
        self.tasks = self.storage.load_tasks() or []

    def add_task(self, title, desc= '',due_date=None):
        task = Task(title, desc, due_date)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
    
    def remove_task(self,title):
        self.tasks = [task for task in self.tasks if task.title!= title]
        self.storage.save_tasks(self.tasks)
    
    def complete_task(self, title):
        task = self.find_task(title)
        if task:
            task.is_complete= True
            self.storage.save_tasks(self.tasks)
            print(f"✅ Task '{title}' marked as completed.")
        else:
            print(f"❌ Task '{title}' not found.")


    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    
    

tm = TaskManager()
#tm.add_task('Code', 'duration: 15 mins daily')
tm.complete_task('Code')
#tm.add_task('Buy cheese', 'Mozorella')
tm.complete_task('Buy cheese')
#tm.remove_task('unload the dishwasher')
tm.list_tasks()