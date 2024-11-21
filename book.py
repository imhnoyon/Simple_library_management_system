from add_books import add_books
from view_all_books import view_all_books

all_books= []
while True:
    print("***********Walcome to Library Management System***********")
    print("1.Add Books")
    print("2.View All Books")
    print("3.Exit")

    Option=input("Select Your Option: ")
    
    if Option=="1":
        add_books(all_books)
        print("BOOKS ADD SUCCESSFULLY")
    elif Option=="2":
        view_all_books(all_books)
    elif Option=="3":
        print("Thanks for using this program")
        break
    else:
        print("Invalid Option")

    

