from add_books import add_books
from view_all_books import view_all_books
from update_book_file import update_books
from delete_book_file import delete_books
from lend_book import lend_book
from return_book import return_book
all_books= []
while True:
    print("\n***********Walcome to Library Management System***********")
    print("1.Add Books")
    print("2.View All Books")
    print("3.Book Update")
    print("4.Book Remove/Delete")
    print("5.Lend Book")
    print("6.Return Book")
    print("7.Exit")
    Option=input("Select Your Option: ")
    
    if Option=="1":
        add_books(all_books)
        print("BOOKS ADD SUCCESSFULLY")
    elif Option=="2":
        view_all_books(all_books)
    elif Option=="3":
        update_books(all_books)

    elif Option=="4":
        delete_books(all_books)

    elif Option=="5":
        lend_book(all_books)

    elif Option=="6":
        return_book()
    
    elif Option=="7":
        print("Thank you for using this program....")
        break
    else:
        print("Invalid Option")

    

