"""
Library Management System

This library project takes input the list of books you want to first display and add it in the list of available books and
it takes your library name as the second input.

We provide five options:
1. Display Books - Display the user passed books (should be the first function to run to add books for the first time)
2. Lend Book - Display the books available. If the book is already owned by someone else, you won't be able to lend
3. Add Book - Add the book you want to add
4. Return Book - Ask you the name and shows the books you own. Select the sr no which you want to return.
5. Exit - Exit from the system
"""


class Library:
    def __init__(self, listOfBooks, libName):
        self.listOfBooks = listOfBooks
        self.libName = libName

    def displayBooks( self,booksLog):
        for item, value in enumerate(self.listOfBooks):
            booksLog[value] = None
        for item,value in booksLog.items():
            print(f"{item}")

    @staticmethod
    def lendBooks(lendBookList, booksLog):
        lendBookList.clear()
        for item, value in enumerate(booksLog):
            print(f"{item + 1}. {value}")
            lendBookList.append(value)
        lendBookNo = int(input("Which book do you want to lend from the above list?\n"))
        lendBook = lendBookList[lendBookNo - 1]
        for item, value in booksLog.items():
            if lendBook == item:
                bookOwner = value
                if bookOwner is not None:
                    print(f"Sorry, {lendBook} is already owned by {bookOwner}. Pls select some other book.")
                else:
                    print("Book is available. Kindly provide your name\n")
                    lenderName = input()
                    print(f"Thank you for choosing {lendBook}, {lenderName}. Happy Reading")
                    booksLog.update({lendBook: lenderName})

    @staticmethod
    def addBooks(booksLog):
        bookName = input("Enter the name of the book you want to add\n")
        booksLog[bookName] = None
        print(f"{bookName} is added in the list of books available.")

    @staticmethod
    def returnBooks(booksLog):
        count = 0
        returnBookList = []
        returneeName = input("Pls enter your name\n")
        print(f"You have the below books on your name {returneeName}:")
        returnBookList.clear()
        for item, value in booksLog.items():
            if value == returneeName:
                print(f"{count + 1}. {item}")
                count += 1
                returnBookList.append(item)
        returnBook = int(input("Pls select the book you want to return\n"))
        returnBookName = returnBookList[returnBook - 1]
        booksLog.update({returnBookName: None})
        print("Thank you for returning the book. Pls visit again.")


chits = Library(["The Journey of Python", "The Cyclone", "Godfather",
                 "Life of a pie", "The White Tiger", "Andaman"], "Keep Learning")
exit = 1
booksLog = {"An Apple": "Chitra"}
lendBookList = []
print("*" * 70)
print(f"Welcome to {chits.libName} Library Management System")
print("*" * 70)
while exit != 0:
    userInput = int(input("Please choose the option (SrNo) from below:\n"
                          "1. Display Books\n"
                          "2. Lend Books\n"
                          "3. Add Books\n"
                          "4. Return Book\n"
                          "5. Exit\n"))
    if userInput == 5:
        exit = 0
    elif userInput == 1:
        chits.displayBooks(booksLog)
    elif userInput == 2:
        chits.lendBooks(lendBookList, booksLog)
    elif userInput == 3:
        chits.addBooks(booksLog)
    elif userInput == 4:
        chits.returnBooks(booksLog)
