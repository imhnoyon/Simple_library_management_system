
# books_file = "all_books.json"
# lend_file = "lends.json"
from lend_book import load_data,lend_file,books_file,save_data



def return_book():
    borrower_name = input("Enter borrower's name: ")
    title = input("Enter the title of the book to return: ")

    lends = load_data(lend_file)
    books = load_data(books_file)

    for lend in lends:
        if lend['borrower_name'].lower() == borrower_name.lower() and lend['title'].lower() == title.lower():
            lends.remove(lend)
            save_data(lend_file, lends)

            for book in books:
                if book['title'].lower() == title.lower():
                    book['quantity'] += 1
                    save_data(books_file, books)
                    print(f"Book '{title}' returned successfully.")
                    return

    print("Lend record not found.")