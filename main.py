import json
import os

def welcome():
    message = ("Welcome to My Library Application. Here you will be able to view, add, edit, and remove books from "
               "your library.")
    print(message)
def create_book_data():
    json_path = './bookdata.json'

    if os.path.exists(json_path):
        return
    else:
        books = {
            'title': ['Great Expectations', '1984', 'Fahrenheit 451']
        }
        with open('bookdata.json', 'w') as outfile:
            json.dump(books, outfile)

def load_data(filepath="bookdata.json"):
    """Loads data from a JSON file."""
    try:
        with open(filepath, "r") as books:
            return json.load(books)
    except FileNotFoundError:
        return []

def save_data(data, filepath="bookdata.json"):
    """Saves data to a JSON file."""
    with open(filepath, "w") as books:
        json.dump(data, books, indent=4)

def add_book(data):
    """Adds a new book to the catalog."""
    book = input(f"Enter title of book: ")
    data['title'].append(book)
    save_data(data)
    print(f"Added {book} to your library")

def list_books(data):
    """Returns a list of all the books in the catalog."""
    if not data:
        print("No items found.")
    else:
        for value in data.values():
            print(value)
            return value
def update_library(data):
    """Updates an existing book in the catalog."""
    library = list_books(data)
    index = int(input("Enter index of book to be replaced: "))
    if 0 <= index < len(library):
        book = input(f"Replace book with: ")
        if book == "":
            return
        book1 = data['title'][index]
        data['title'][index] = book
        save_data(data)
        print(f"Replaced '{book1}' with '{book}'")
    else:
        print("Invalid index.")

def delete_book(data):
    """Deletes an book from the catalog."""
    library = list_books(data)
    index = int(input("Enter index of book to remove: "))
    if 0 <= index < len(library):
        book1 = data['title'][index]
        answer = input(f"Are you sure you would like to remove this book? (Y/N): ")
        if answer == 'Y':
            del data['title'][index]
            save_data(data)
            print(f"'{book1}' successfully removed from library")
        else:
            print("Returning to Main Menu")
            return
    else:
        print("Invalid index.")

if __name__ == "__main__":
    create_book_data()
    data = load_data()
    welcome()

    while True:
        print("\nMain Menu:")
        print("Use options 1-5 or the key word contained in parentheses to to select an option.")
        print("1. Add a book (Add)")
        print("2. Get a list of books (Get)")
        print("3. Update library (Update)")
        print("4. Delete a book form library (Delete)")
        print("5. Exit (Exit)")

        choice = input("Enter your choice: ")

        if choice == "1" or choice == "Add":
            add_book(data)
        elif choice == "2" or choice == "Get":
            list_books(data)
        elif choice == "3" or choice == "Update":
            update_library(data)
        elif choice == "4" or choice == "Delete":
            delete_book(data)
        elif choice == "5" or choice == "Exit":
            break
        else:
            print("Invalid choice.")
