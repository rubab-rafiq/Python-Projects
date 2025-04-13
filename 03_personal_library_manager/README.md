# 📚 Personal Library App

A simple and interactive **Streamlit** web application to manage your personal library. You can add, view, search, and remove books, as well as track how many you've read and unread.

---

## 🚀 Features

- ➕ **Add Book** – Add book details including title, author, year, genre, and read status.  
- 📖 **View Books** – See all your saved books in a table format.  
- ❌ **Remove Book** – Remove any book from your library.  
- 🔍 **Search Book** – Find books by title or author.  
- 📊 **Statistics** – View total books, how many are read or unread.

---

## 🛠️ Technologies Used

- Python  
- Streamlit  
- JSON (for saving book data)

---

## 📁 File Structure

📂 personal-library-app/ ├── 📄 app.py # Main Streamlit application ├── 📄 library.json # Stores book data └── 📄 README.md # Project info

yaml
Copy
Edit

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/rubab-rafiq/personal-library-app.git
cd personal-library-app
Install Streamlit:

bash
Copy
Edit
pip install streamlit
Run the app:

bash
Copy
Edit
streamlit run app.py
📌 Example Book Entry
json
Copy
Edit
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "year": 1925,
  "genre": "Literary Fiction",
  "read_status": true
}
🙋 Author
Made with ❤️ by Rubab M.Rafiq

