import json

from dad_joke import DadJoke


class Database:
    def __init__(self, filename='db.json'):
        self.jokes = []
        self.filename = filename
        self.read_from_file()

    def add_record(self, record):
        self.jokes.append(record)

    def get_records(self):
        return self.jokes

    def save_to_file(self):
        json_string = json.dumps([ob.__dict__ for ob in self.jokes])
        with open(self.filename, 'w') as file:
            file.write(json_string)

    def read_from_file(self):
        with open(self.filename, 'r') as file:
            jokes = json.load(file, object_hook=lambda d: DadJoke(**d))
            self.jokes = jokes
