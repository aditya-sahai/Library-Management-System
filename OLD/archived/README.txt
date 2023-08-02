Project :- Library Management System

##################################################
#                                                #
#   run main_menu.py to run the entire project   #
#                                                #
##################################################

The project stores information about the books owned by a library.
Library owner can add books to the database (stored in CSV format) whenever the owner
buys a book for the library.
The code keeps track of issued books by storing the name of the borrower and date on
which the book was issued.

The project has 4 options :-
[1] Enter New Book
[2] Issue Book
[3] Return Book
[4] Check Book Status

[1] Enter New Book
When the owner of the library buys a new book for the library and to save it
in the CSV files.

[2] Issue Book
When a borrower wants to issue a book.

[3] Return Book
When a borrower wants to return an issued book.

[4] Check Book Status
Displays the information stored about a particular book entered.
If book is found it displays: name, author, ISBN and if it issued by someone
or not (also displays name of borrower and date of issuing the book).

Purpose of each file :-
There are 4 categories of program files.
1. main_menu.py (the main file)
2. CRUD_Operations.py (has functions JUST for reading and updating CSV files)
3. GUI files (has functions for running the GUI)

1. main_menu.py has code for the running the main window where the 4 options are shown.
All the other files are imported in this file and required function is called
depending the requirement.

2. CRUDOperations.py has functions for Creating, Reading, Updating and Deleting records
from the files. Only responsible for processing the data. (backend)

3. GUI files include book_status.py, issue_book.py, new_book.py and return_book.py.
GUI files are only responsible for the GUI and no processing is done here. (frontend)
These files have functions for running the GUI for option 4, 2, 1 and 3 respectively.

The project also has a folder called 'books' which contains 5 CSV files.
Each shelf (genre) has its own file.

Developers :-
Aditya Sahai (XI - S2), Krish Ghorse (XI - S2), Sara Gupta (XI - S2)
