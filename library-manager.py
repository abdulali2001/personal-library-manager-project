#Library Management System - Python Project
#A library management system keeps track of the books present in the library. It is an important piece of software which is a must at schools and colleges

book_list = list()

#menu items
menu = """
1) Add Book
2) Remove Book
3) View Book
4) Press E to Exit
"""
#add books
def add_book(booklist, book):
    booklist.append(book)
    print("Book added successfully")

#removed books
def remove_book(booklist, book):
    if book in booklist:
       booklist.remove(book)
       print("Book remove successfully")
    else:
        print("Book not found in this list")

#display all books results
def display_list(booklist):
    if booklist:
        print("Added Books ->", ", ".join(booklist))
    else:
        print("No books in the list")

#exit program
def exit_program():
    print("Thank you for visiting the book library system.")
    quit()

#main program loop
while True:
    print(menu)
    choice = input("Your choice: ")

    if choice == "1": #add book
        book_name == input("Enter the book name you want to add:")
        add_book(book_list, book_name)

    elif choice == "2" #remove book
         book_name = input("Enter the book name to remove: ")

    elif choice == "3" #view book list
         display_list(book_list)

    elif choice.lower() == "e": #exit program
         exit_program()

    else:
        print("Invalid entry")
        input("press enter to return to the main menu!")