class Phonebook2:

    def __init__(self):
        self.number = {}

    def add(self, name, number):
        self.number[name] = number

    def find(self, name):
        return self.number[name]

    def get_names(self):
        return set(self.number.keys())

    def clear(self):
        pass
