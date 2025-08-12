from datetime import datetime

class Task:
    def __init__(self, title, desc='', due_date = None, created_at=None):
        self.title = title
        self.desc = desc
        self.due_date = due_date
        self.is_complete = False
        self.created_at = created_at or datetime.now()
        #print(self.created_at)

    def mark_complete(self):
        self.is_complete = True

    def mark_incomplete(self):
        self.is_complete = False

    def __str__(self):
        status = "✔️ " if self.is_complete else "❌"
        due = f'Due: {self.due_date}' if self.due_date else ""
        return f'''{status} {self.title}{due} - {self.desc}\n⬜ Created at: {str(self.created_at)[:11]}'''

