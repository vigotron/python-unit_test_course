import pytest


class Phonebook:

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


@pytest.fixture()
def phonebook():
    return Phonebook()


def test_lookup_by_name(phonebook):
    phonebook.add("Juanjo", "678445533")
    assert "678445533" == phonebook.find("Juanjo")


def test_get_all_names(phonebook):
    phonebook.add("Juanjo", "678445533")
    phonebook.add("Joel", "778445533")
    phonebook.add("Chris", "878445533")
    assert phonebook.get_names() == {"Juanjo", "Joel", "Chris"}
    assert "Joel" in phonebook.get_names()


def test_missing_name_raises_exception(phonebook):
    with pytest.raises(KeyError):
        phonebook.find("m")
