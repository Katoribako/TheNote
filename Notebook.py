import json
from datetime import datetime

from Note import Note


class Notebook:
    def __init__(self, filename):
        self.notes = []
        self.filename = filename

    def load_notes(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.notes = [Note(note["id"], note["title"], note["content"]) for note in data]
        except FileNotFoundError:
            pass

    def save_notes(self):
        data = [{"id": note.id, "title": note.title, "content": note.content} for note in self.notes]
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def add_note(self, title, content):
        id = max([note.id for note in self.notes]) + 1 if self.notes else 1
        note = Note(id, title, content)
        self.notes.append(note)

    def edit_note(self, id, title, content):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.content = content
                note.timestamp = datetime.now()
                break

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]

    def delete_all_notes(self):
        self.notes = []

    def get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def get_notes_by_date(self, date):
        return [note for note in self.notes if note.timestamp.date() == date]

    def display_notes(self):
        for note in self.notes:
            print(note)

    def get_last_note_id(self):
        if self.notes:
            return self.notes[-1].id
        else:
            return 0