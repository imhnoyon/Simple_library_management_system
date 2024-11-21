
def view_all_books(all_books):
    if all_books !=[]:
        print("BookName----Author----isbn----year----price----quantity")
        for book in all_books:
            print(f"{book["title"]}------{book["author"]}------{book["isbn"]}------{book["year"]}------{book["price"]}------{book["quantity"]} \n")

    else:
        print("No book here")
