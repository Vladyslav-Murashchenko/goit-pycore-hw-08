from src.parsers import parse_input
from src.handlers import add_phone, change_phone, show_contact, show_all, add_birthday, show_birthday, birthdays
from src.persist import load_data, save_data

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_phone(args, book))
        elif command == "change":
            print(change_phone(args, book))
        elif command == "phone":
            print(show_contact(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        elif command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
