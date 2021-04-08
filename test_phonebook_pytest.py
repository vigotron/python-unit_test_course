import pytest

from phonebook2 import Phonebook2


@pytest.fixture()
def phonebook(tmpdir):
    "Provides a temporary Phonebook"
    "pytest --fixtures"
    return Phonebook2(tmpdir)
    #yield phonebook
    #phonebook.clear()


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
