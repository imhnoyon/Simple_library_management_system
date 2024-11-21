def save_books(all_books):
    with open("all_book.txt","w") as file:
        for book in all_books:
            line=f"{book["title"]} {book["author"]} {book["isbn"]} {book["year"]} {book["price"]} {book["quantity"]} \n"
            file.write(line)