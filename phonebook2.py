import os


class Phonebook2:

    def __init__(self, cache_folder):
        self.number = {}
        self.fileName = os.path.join(cache_folder, "cache.txt")
        self.cache = open(self.fileName, "w")

    def add(self, name, number):
        self.number[name] = number

    def find(self, name):
        return self.number[name]

    def get_names(self):
        return set(self.number.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.fileName)
