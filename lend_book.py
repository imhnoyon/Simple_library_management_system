import json
from datetime import datetime, timedelta
from view_all_books import view_all_books
# from book import all_books


books_file = "all_books.json"
lend_file = "lends.json"


def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

        
def lend_book(all_books):
    view_all_books(all_books)
    title = input("Enter the title of the book to lend: ")
    books = load_data(books_file)

    for book in books:
        if book['title'].lower() == title.lower():
            if book['quantity'] <= 0:
                print("There are not enough books available to lend.")
                return
            
            borrower_name = input("Enter borrower's name: ")
            phone = input("Enter borrower's phone number: ")
            due_date = datetime.now() + timedelta(days=14)

            lends = load_data(lend_file)
            lends.append({
                "borrower_name": borrower_name,
                "phone": phone,
                "title": book['title'],
                "due_date": due_date.strftime('%Y-%m-%d')
            })
            save_data(lend_file, lends)

            book['quantity'] -= 1
            save_data(books_file, books)

            print(f"Book '{title}' lent to {borrower_name}. Return due date: {due_date.strftime('%Y-%m-%d')}.")
            return

    print("Book not found.")
