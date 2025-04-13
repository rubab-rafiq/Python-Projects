
import streamlit as st
import json

# File to store data
FILE = "library.json"

# Load books
def load_books():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save books
def save_books(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Load data on start
books = load_books()

# Page setup
st.set_page_config(page_title="Library", page_icon="📚", layout="wide")
st.title("📚 Personal Library")
st.markdown("---")

# Sidebar menu
menu = st.sidebar.radio("Choose Option", ["Add Book", "View Books", "Remove Book", "Search Book", "Statistics"])

# View Books
if menu == "View Books":
    st.header("📖 Your Books")
    if books:
        st.table(books)
    else:
        st.info("No books added yet.")

# Add Book
elif menu == "Add Book":
    st.header("➕ Add Book")
    with st.form("form_add"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.number_input("Year", 1910, 2025)
        genre = st.text_input("Genre")
        read = st.checkbox("Read?")
        submit = st.form_submit_button("Add")
        
        if submit:
            if title and author and genre:
                books.append({"title": title, "author": author, "year": year, "genre": genre, "read_status": read})
                save_books(books)
                st.success("Book Added!")
            else:
                st.error("Please fill all fields.")

# Remove Book
elif menu == "Remove Book":
    st.header("❌ Remove Book")
    if books:
        options = [b["title"] for b in books]
        choice = st.selectbox("Select book", options)
        if st.button("Remove"):
            books = [b for b in books if b["title"] != choice]
            save_books(books)
            st.success("Book Removed!")
    else:
        st.warning("Library is empty.")

# Search Book
elif menu == "Search Book":
    st.header("🔍 Search")
    term = st.text_input("Enter title or author")
    if st.button("Search"):
        results = [b for b in books if term.lower() in b["title"].lower() or term.lower() in b["author"].lower()]
        if results:
            st.table(results)
        else:
            st.warning("No matching book found.")

# Stats
elif menu == "Statistics":
    st.header("📊 Stats")
    total = len(books)
    read = sum(1 for b in books if b["read_status"])
    unread = total - read

    st.metric("Total Books", total)
    st.metric("Read", read)
    st.metric("Unread", unread)
