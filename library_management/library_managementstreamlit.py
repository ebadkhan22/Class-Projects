import streamlit as st
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

def add_book(library, title, author, year, genre, read_status):
    """Add a new book to the library."""
    library.append({
        "Title": title,
        "Author": author,
        "Year": int(year),
        "Genre": genre,
        "Read": read_status
    })
    save_library(library)

def remove_book(library, title):
    """Remove a book from the library by title."""
    library[:] = [book for book in library if book["Title"].lower() != title.lower()]
    save_library(library)

def search_books(library, keyword):
    """Search for books by title or author."""
    return [book for book in library if keyword.lower() in book["Title"].lower() or keyword.lower() in book["Author"].lower()]

def display_statistics(library):
    """Display statistics of the library."""
    total_books = len(library)
    read_books = sum(book["Read"] for book in library)
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
    return total_books, read_percentage

# Load existing library data
library = load_library()

# Streamlit UI
st.title("📚 Personal Library Manager")

menu = ["Add Book", "Remove Book", "Search Book", "View All Books", "Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Mark as Read")
    if st.button("Add Book"):
        add_book(library, title, author, year, genre, read_status)
        st.success("Book added successfully!")

elif choice == "Remove Book":
    st.subheader("Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove Book"):
        remove_book(library, title)
        st.success("Book removed successfully!")

elif choice == "Search Book":
    st.subheader("Search for a Book")
    keyword = st.text_input("Enter book title or author")
    if st.button("Search"):
        results = search_books(library, keyword)
        if results:
            for book in results:
                st.write(f"📖 **{book['Title']}** by {book['Author']} ({book['Year']}) - {book['Genre']} - {'✅ Read' if book['Read'] else '❌ Unread'}")
        else:
            st.warning("No matching books found!")

elif choice == "View All Books":
    st.subheader("Your Library")
    if library:
        for book in library:
            st.write(f"📖 **{book['Title']}** by {book['Author']} ({book['Year']}) - {book['Genre']} - {'✅ Read' if book['Read'] else '❌ Unread'}")
    else:
        st.info("Your library is empty!")

elif choice == "Statistics":
    st.subheader("Library Statistics")
    total_books, read_percentage = display_statistics(library)
    st.write(f"📚 **Total books:** {total_books}")
    st.write(f"✅ **Percentage read:** {read_percentage:.2f}%")
