#Author: Lock Yan Fong, Brendon
#Admin Number / Grp:230739G / AA2303


book_type = ["Paper Back", "Hard Cover", "eBook"]

initial_books = [
    ["978-0134846019", "Data Analytics with Spark Using Python", 0, 6],
    ["978-0133316032", "Children's Reading", 2, 3],
    ["978-1292100142", "Global Marketing, 7th Edition", 2, 8],
    ["978-1587147029", "CCNA Cyber Ops SECFND #210-250 Official Cert Guide", 1, 5],
    ["0306406152", "Learn Data Analytics in 100 days", 0, 10]
]

books = initial_books.copy()   #Duplicates the contents of the list into a new list. Will have the same elements as the original list, but they are independent copies.(allows me to keep
                               #the books already inputted and continue to carry out whatever functions wanted.

def validate_isbn(isbn):
    if len(isbn) == 10:
        if not isbn.isdigit():
            return False
    elif len(isbn) == 14:
        if not isbn[:3].isdigit() or isbn[3] != '-' or not isbn[4:].isdigit():
            return False
    else:
        return False
    return True

def add_book(new_book):
    global books
    isbn = new_book[0]
    if not validate_isbn(isbn):
        print("Invalid ISBN format. Book not added to the library.")
        return
    
    books.append(new_book)
    print(f"{new_book[1]} has been added to the library.")

def view_books():
    global books
    if books:
        for index, book in enumerate(books, start=1):   #allows me to iterate over the list of books and keeps track of the position and value of each item in my book list
            print(f"{index}. ISBN: {book[0]}, Title: {book[1]}, Type: {book_type[book[2]]}, Quantity: {book[3]}")
    else:
        print("The library is empty.")        #if there is no books in the library


def remove_book_by_index(index):
    global books
    if 0 <= index < len(books):
        removed_book = books.pop(index)
        print(f"{removed_book[1]} has been removed from the library.")
    else:
        print("Invalid index number. No book removed.")


def update_quantity_by_index(index, new_quantity):
    global books
    if 0 <= index < len(books):
        books[index][3] = new_quantity
        print(f"Quantity for {books[index][1]} has been updated to {new_quantity}.")
    else:
        print("Invalid number. Quantity not updated.")

def update_book_type_by_index(index, new_book_type_id):
    global books, book_type
    if 0 <= index < len(books) and 0 <= new_book_type_id < len(book_type):
        books[index][2] = new_book_type_id
        print(f"Book type for {books[index][1]} has been updated to {book_type[new_book_type_id]}.")
    else:
        print("Invalid number or book type. Book type not updated.")

def update_isbn_by_index(index, new_isbn):
    global books
    if 0 <= index < len(books) and validate_isbn(new_isbn):
        books[index][0] = new_isbn
        print(f"ISBN for {books[index][1]} has been updated to {new_isbn}.")
    else:
        print("Invalid number or ISBN format. ISBN not updated.")

def update_title_by_index(index, new_title):
    global books
    if 0 <= index < len(books):
        books[index][1] = new_title
        print(f"Title has been updated to {new_title}.")
    else:
        print("Invalid number. Title not updated.")





#main menu
        
while True:
    print("\nWelcome to the Mini Library System! What can I do for you?")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Quit")
    
    choice = input("Enter your choice: ")

    #Add book
    if choice == '1':
        while True:
            isbn = input("Enter the ISBN of the new book (10 or 13 digits): ")
            if validate_isbn(isbn):
                break
            else:
                print("Invalid ISBN format. It has to be 10 digits only (eg.1234567890) or 13 digits including a hyphen(eg. 978-1234567890)")
                
        title = input("Enter the title of the new book: ")
        while True:
            print("Available book types:")
            for i, type_name in enumerate(book_type):
                print(f"{i}. {type_name}")
            book_type_id = int(input("Enter the type of the book (0, 1, or 2): "))
            if 0 <= book_type_id < len(book_type):
                break
            else:
                print("Invalid book type. Please enter a valid type.")

        while True:
            quantity = input("Enter the quantity of the book: ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Invalid quantity. Please enter a valid number.")
        
        new_book = [isbn, title, book_type_id, quantity]
        add_book(new_book)
    
    #View books    
    elif choice == '2':
        print("\nBooks in the library:")
        view_books()
        total_quantity = sum(book[3] for book in books)
        print(f"\nThere are a total of {total_quantity} books in the library.")
    
    #Update book    
    elif choice == '3':
        print("\nBooks in the library:")
        view_books()
        print("")
        
        while True:             #loop until valid input is entered then run this while loop
            try:                #execute the code
                index_to_update = int(input("Enter the number(eg. 1,2,3,etc.) for the book you want to update: "))
                if 1 <= index_to_update <= len(books):
                    break
                else:
                    print("Invalid number. Please enter a valid number.")
            except ValueError:         #if the user enter non numerical value, this line and the following one will run
                print("Invalid input. Please enter a valid number.")
        
        book_to_update = books[index_to_update - 1]        #make the index_to_update variable be back to zero as lists use 0 based indexing
                                                           #as we made the book index start from 1 in our view books function at the top
        print(f"\nSelected book: {book_to_update[1]}")
        
        print("\nWhat do you want to update?")
        print("1. Quantity")
        print("2. Book Type")
        print("3. ISBN Number")
        print("4. Book Name")
        
        update_option = input("Enter your choice: ")
        
        if update_option == '1':
            new_quantity = int(input("Enter the new quantity: "))
            update_quantity_by_index(index_to_update - 1, new_quantity)
        elif update_option == '2':
            new_book_type_id = int(input("Enter the new book type (0, 1, or 2): "))
            update_book_type_by_index(index_to_update - 1, new_book_type_id)
        elif update_option == '3':
            new_isbn = input("Enter the new ISBN (10 or 13 digits): ")
            update_isbn_by_index(index_to_update - 1, new_isbn)
        elif update_option == '4':
            new_title = input("Enter the new title: ")
            update_title_by_index(index_to_update - 1, new_title)
        else:
            print("Invalid choice. Please select a valid option.")

    #Remove book
    elif choice == '4':
        print("\nBooks in the library:")
        view_books()
        print("")
        
        while True:
            try:
                index_to_remove = int(input("Enter the number(eg. 1,2,3,etc.)for the book you want to remove: "))
                if 1 <= index_to_remove <= len(books):
                    break
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        remove_book_by_index(index_to_remove - 1)

    #Quit
    elif choice == '5':
        print("Goodbye, Have a nice day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")



