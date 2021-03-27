import unittest

from phonebook import PhoneBook


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def test_find_number_by_name(self):
        self.phonebook.add("Juan", "667894567")
        number = self.phonebook.find("Juan")
        self.assertEqual("667894567", number)

    def test_find_name_by_number(self):
        with self.assertRaises(KeyError):
            self.phonebook.find("Missing")

    def test_consistent_when_empty(self):
        self.phonebook.add("", "")
        self.assertTrue(self.phonebook.is_consistent())

    def test_consistent_with_different_entries(self):
        self.phonebook.add("Kim", "23456")
        self.phonebook.add("Roy", "23456567")
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicated_number(self):
        self.phonebook.add("Joe", "123456")
        self.phonebook.add("Kogan", "123456")
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_same_prefix(self):
        self.phonebook.add("Jim", "123456")
        self.phonebook.add("Sofie", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_name_and_number(self):
        self.phonebook.add("John", "33344455")
        self.phonebook.add("Ben", "33347864")
        self.assertIn("John", self.phonebook.get_names())
        self.assertIn("33344455", self.phonebook.get_numbers())

    # def test_remove_phonebook_number(self):
    #     self.phonebook.add("John", "33344455")
    #     self.phonebook.add("Ben", "33347864")
    #     self.phonebook.remove_by_name("John")
    #     self.assertNotIn("John", self.phonebook.get_names())
    #     self.assertIn("Ben", self.phonebook.get_names())
