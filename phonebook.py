class PhoneBook:

    def __init__(self):
        self.number = {}
        self.name = ""

    def add(self, name, number):
        self.number[name] = number

    def find(self, name):
        return self.number[name]

    def is_consistent(self):
        for name1, number1 in self.number.items():
            for name2, number2 in self.number.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
            return True

    def get_names(self):
        key_list = []
        for names in self.number.keys():
            key_list.append(names)
        return key_list

    def get_numbers(self):
        value_list = []
        for number in self.number.values():
            value_list.append(number)
        return value_list

    def remove_by_name(self, name_to_remove):
        for name, number in list(self.number.items()):
            if name == name_to_remove:
                del self.number[name_to_remove]
