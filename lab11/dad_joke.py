class DadJoke:
    def __init__(self, id=0, joke="", status=200):
        self.id = id
        self.joke = joke
        self.status = status

    def __str__(self):
        return f"DadJoke(id={self.id}, joke={self.joke}, status={self.status})"

    def __repr__(self):
        return self.__str__()