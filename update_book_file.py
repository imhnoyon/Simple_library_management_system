import save_all_books
from datetime import datetime

def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"] == search_book:
            title = input("Enter Book to New Title: ")
            author = input("Enter Author Name: ")
            year = int(input("Enter Publishing Year Number: "))
            price = int(input("Enter Book Price: "))
            quantity = int(input("Enter Quantity Number: "))

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdatedAt"] = book_last_updated_at

            save_all_books.save_books(all_books)
            print("Book Updated Successfully")
            return all_books

    print("Book Not Found")