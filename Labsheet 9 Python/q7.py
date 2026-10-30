books = []

while True:
    print("\n1. Add book")
    print("2. View books")
    print("3. Update book")
    print("4. Delete book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added")

    elif choice == "2":
        for book in books:
            print(book)

    elif choice == "3":
        old = input("Enter book name to update: ")
        if old in books:
            new = input("Enter new book name: ")
            books[books.index(old)] = new
            print("Book updated")
        else:
            print("Book not found")

    elif choice == "4":
        book = input("Enter book name to delete: ")
        if book in books:
            books.remove(book)
            print("Book deleted")
        else:
            print("Book not found")

    elif choice == "5":
        break

    else:
        print("Invalid choice")