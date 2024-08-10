from src.address_book import AddressBook, Record, UPCOMING_BIRTHDAY_THRESHOLD
from src.errors import NameNotFound, PhoneNotFound, IncorrectName, IncorrectPhone, InvalidDate, ArgsCountError

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "This command require 2 arguments."
        except IndexError:
            return "This command require 1 argument."
        except (
            NameNotFound,
            PhoneNotFound,
            IncorrectName,
            IncorrectPhone,
            InvalidDate,
            ArgsCountError
        ) as error:
            return str(error)

    return inner

@input_error
def add_phone(args, book: AddressBook):
    name, phone = args

    record = book.data[name] if name in book.data else Record(name)
    record.add_phone(phone)

    if name not in book.data:
        book.add_record(record)

    return "Phone added."

@input_error
def change_phone(args, book: AddressBook):
    if (len(args) != 3):
        raise ArgsCountError("This command require 3 arguments.")

    name, old_phone, new_phone = args

    record = book.find(name)
    record.edit_phone(old_phone, new_phone)

    return "Phone updated."

@input_error
def show_contact(args, book: AddressBook):
    name = args[0]

    record = book.find(name)

    return str(record)

def show_all(book: AddressBook):
    records = book.data.values()

    return "\n".join([str(record) for record in records])

@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args

    record = book.find(name)
    record.add_birthday(birthday)

    return "Birthday added."

@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]

    record = book.find(name)

    return f"{record.name.value}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"

@input_error
def birthdays(book: AddressBook):
    persons = book.get_upcoming_birthdays()

    if not persons:
        return f"No birthdays in the next {UPCOMING_BIRTHDAY_THRESHOLD} days."

    return "\n".join([get_birthday_message(person) for person in persons])

def get_birthday_message(person):
    return f"{person['name']}'s congratulation date is {person['congratulation_date']}"
