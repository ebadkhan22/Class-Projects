import json

# File to store library data
LIBRARY_FILE = "library.json"


def load_library():
    """Load the library from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_library(library):
    """Save the library to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)


def add_book(library):
    """Add a new book to the library."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    library.append({
        "Title": title,
        "Author": author,
        "Year": int(year),
        "Genre": genre,
        "Read": read_status
    })
    print("Book added successfully!\n")


def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["Title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!\n")
            return
    print("Book not found!\n")


def search_book(library):
    """Search for a book by title or author."""
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    keyword = input("Enter the search term: ").lower()
    results = [book for book in library if keyword in book["Title"].lower() or keyword in book["Author"].lower()]

    if results:
        print("Matching Books:")
        for i, book in enumerate(results, 1):
            print(
                f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
    else:
        print("No matching books found!\n")


def display_books(library):
    """Display all books in the library."""
    if not library:
        print("Your library is empty!\n")
        return

    print("Your Library:")
    for i, book in enumerate(library, 1):
        print(
            f"{i}. {book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
    print()


def display_statistics(library):
    """Display statistics of the library."""
    total_books = len(library)
    read_books = sum(book["Read"] for book in library)
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.2f}%\n")


def main():
    """Main function to run the Personal Library Manager."""
    library = load_library()

    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    main()
