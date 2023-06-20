import datetime

class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.id}. {self.title} ({self.timestamp.strftime('%Y-%m-%d %H:%M:%S')})"