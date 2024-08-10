import pickle
from src.address_book import AddressBook

FILE_NAME = "address_book.pkl"

def save_data(book: AddressBook):
    with open(FILE_NAME, "wb") as file:
        pickle.dump(book, file)

def load_data() -> AddressBook:
    try:
        with open(FILE_NAME, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
