from save_all_books import save_books
import random
from datetime import datetime
def add_books(all_books):
    title=input("Enter Your book title: ")
    author=input("Enter Your Author Name: ")
    # isbn= int(input("Enter isbn Number: "))
    year=int(input("Enter publishing Year: "))
    price=int(input("Enter book price: "))
    # quantity=int(input("Book Quantity: "))
     

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book={
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
        "bookAddedAt": bookAddedAt,
        "bookLastUpdatedAt": ""
    }
 
    all_books.append(book)
    save_books(all_books)
    return all_books
