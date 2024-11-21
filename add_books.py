from save_all_books import save_books

def add_books(all_books):
    title=input("Enter Your book title: ")
    author=input("Enter Your Author Name: ")
    isbn= int(input("Enter isbn Number: "))
    year=int(input("Enter publishing Year: "))
    price=int(input("Enter book price: "))
    quantity=int(input("Book Quantity: "))

    book={
        "title":title,
        "author":author,
        "isbn":isbn,
        "year":year,
        "price":price,
        "quantity":quantity,
    }
 
    all_books.append(book)
    save_books(all_books)
    return all_books
