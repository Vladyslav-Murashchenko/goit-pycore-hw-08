from datetime import datetime
from src.errors import IncorrectName, IncorrectPhone, InvalidDate

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        self.value = self.validate(name)

    def validate(self, name):
        if not name:
            raise IncorrectName("Name can't be empty")
        return name

class Phone(Field):
    def __init__(self, phone):
        self.value = self.validate(phone)

    def validate(self, phone):
        if not phone.isdigit():
            raise IncorrectPhone("Phone number must contain only digits")
        if len(phone) != 10:
            raise IncorrectPhone("Phone number must be 10 digits long")
        return phone

class Birthday(Field):
    def __init__(self, birthday):
        self.value = self.validate(birthday)

    def validate(self, birthday):
        try:
            return datetime.strptime(birthday, "%d.%m.%Y")
        except ValueError:
            raise InvalidDate("Invalid date format. Use DD.MM.YYYY")
