# Create your models here.

class Task(dict):
    def __init__(self, title, complete, created):
        self.title = title
        self.complete = complete
        self.created = created
        super().__init__(title=title, complete=complete, created=created)

