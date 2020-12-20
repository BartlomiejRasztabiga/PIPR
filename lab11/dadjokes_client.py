import requests

from dad_joke import DadJoke
from database import Database


class DadJokesClient:
    def __init__(self, db_filename):
        self.database = Database(db_filename)

    def fetch_random_dad_joke(self):
        response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
        return response.json(object_hook=lambda d: DadJoke(**d))

    def add_favorite_joke(self, joke):
        self.database.add_record(joke)

    def save_favorite_jokes(self):
        self.database.save_to_file()

    def run(self):
        while True:
            joke = self.fetch_random_dad_joke()
            print(joke.joke)
            response = input('Was the joke good enough? (Y/n)')
            if response == 'Y':
                self.add_favorite_joke(joke)
            response = input("Do you want to stop? (Y/n)")
            if response == 'Y':
                self.save_favorite_jokes()
                break


def main():
    client = DadJokesClient('db.json')
    client.run()


if __name__ == "__main__":
    main()
