# Library_Management_Python
import tkinter as tk
from tkinter import simpledialog, messagebox

class Library:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x350")
        self.root.resizable(False, False)
        self.root.configure(bg="#ecf0f1")

        # Books with ID
        self.books = {
            101: "Python Basics",
            102: "Data Structures",
            103: "Machine Learning"
        }

        self.issued_books = {}

        self.create_menu()

    def create_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="📚 Library Management System",
                 font=("Helvetica", 18, "bold"),
                 fg="#2c3e50", bg="#ecf0f1").pack(pady=20)

        tk.Button(self.root, text="View Books", command=self.view_books,
                  bg="#3498db", fg="white", width=25, height=2).pack(pady=5)

        tk.Button(self.root, text="Issue Book", command=self.issue_book,
                  bg="#2ecc71", fg="white", width=25, height=2).pack(pady=5)

        tk.Button(self.root, text="Return Book", command=self.return_book,
                  bg="#f39c12", fg="white", width=25, height=2).pack(pady=5)

        tk.Button(self.root, text="Add Book", command=self.add_book,
                  bg="#9b59b6", fg="white", width=25, height=2).pack(pady=5)

        tk.Button(self.root, text="Exit", command=self.root.quit,
                  bg="#e74c3c", fg="white", width=25, height=2).pack(pady=5)

    def view_books(self):
        if not self.books:
            messagebox.showinfo("Books", "No books available")
            return

        text = ""
        for book_id, name in self.books.items():
            text += f"ID: {book_id} | {name}\n"

        messagebox.showinfo("Available Books", text)

    def issue_book(self):
        try:
            book_id = int(simpledialog.askstring("Issue Book", "Enter Book ID:"))
            if book_id in self.books:
                book_name = self.books[book_id]
                self.issued_books[book_id] = self.books.pop(book_id)

                messagebox.showinfo(
                    "Success",
                    f"Book Issued Successfully!\n\nID: {book_id}\nName: {book_name}"
                )
            else:
                messagebox.showerror("Error", "Invalid Book ID")
        except:
            messagebox.showerror("Error", "Enter valid ID")

    def return_book(self):
        try:
            book_id = int(simpledialog.askstring("Return Book", "Enter Book ID:"))
            if book_id in self.issued_books:
                book_name = self.issued_books[book_id]
                self.books[book_id] = self.issued_books.pop(book_id)

                messagebox.showinfo(
                    "Success",
                    f"Book Returned Successfully!\n\nID: {book_id}\nName: {book_name}"
                )
            else:
                messagebox.showerror("Error", "Invalid Book ID")
        except:
            messagebox.showerror("Error", "Enter valid ID")

    def add_book(self):
        name = simpledialog.askstring("Add Book", "Enter Book Name:")
        if name:
            new_id = max(self.books.keys(), default=100) + 1
            self.books[new_id] = name

            messagebox.showinfo(
                "Success",
                f"Book Added Successfully!\n\nID: {new_id}\nName: {name}"
            )

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = Library(root)
    root.mainloop()
