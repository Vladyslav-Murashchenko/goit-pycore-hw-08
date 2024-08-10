from datetime import datetime, timedelta
from collections import UserDict
from src.errors import NameNotFound, PhoneNotFound
from src.fields import Name, Phone, Birthday

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = phone.validate(new_phone)
                return
        raise PhoneNotFound(f"Phone {old_phone} not found")

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return phone
        raise PhoneNotFound(f"Phone {phone} not found")

    def remove_phone(self, phone_to_remove):
        for phone in self.phones:
            if phone.value == phone_to_remove:
                self.phones.remove(phone)
                return
        raise PhoneNotFound(f"Phone {phone} not found")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

UPCOMING_BIRTHDAY_THRESHOLD = 7

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return
        raise NameNotFound(f"Record with name {name} not found")

    def find(self, name) -> Record:
        if name in self.data:
            return self.data[name]
        raise NameNotFound(f"Record with name {name} not found")

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday = record.birthday.value
            next_birthday = datetime(today.year, birthday.month, birthday.day).date()

            if (next_birthday < today):
                next_birthday = datetime(today.year + 1, birthday.month, birthday.day).date()

            days_until_birthday = (next_birthday - today).days

            if (days_until_birthday > UPCOMING_BIRTHDAY_THRESHOLD):
                continue

            congratulation_date = next_birthday

            if congratulation_date.weekday() >= 5:
                days_to_add = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_add)

            upcoming_birthdays.append({
                'name': record.name.value,
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

        return upcoming_birthdays
