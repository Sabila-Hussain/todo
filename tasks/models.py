# Create your models here.

class Task(dict):
    def __init__(self, title):
        self.title = title
        self.complete = False
        super().__init__(title=self.title, complete=self.complete)

