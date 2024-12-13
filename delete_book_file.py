import save_all_books

def delete_books(all_books):
    search_book = input("Enter Book Title to Delete: ")
    for book in all_books:
        if book["title"] == search_book:
            all_books.remove(book)
            save_all_books.save_books(all_books)
            print("Book Deleted Successfully")
            return all_books
    
    print("Book Not Found")