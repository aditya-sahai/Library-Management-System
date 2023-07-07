import os
import csv


BOOKS_FILE = os.path.join(os.getcwd(), "books.csv")
USERS_FILE = os.path.join(os.getcwd(), "users.csv")

def reset_data_files(reset_books=True, reset_users=True):
    """
    Removes all the data from the books and users file if reset_books and reset_users respectively
    are True
    """
    # NOT USED IN PROGRAM, MADE ONLY FOR CONVENIENCE WHILE DEVELOPING
    if reset_books:
        with open(BOOKS_FILE, "w", newline="") as books_f:
            books_f.write("Book Name,Genre,ISBN,Author,Status")
    if reset_users:
        with open(USERS_FILE, "w", newline="") as users_f:
            users_f.write("First Name, Last Name,Phone")

def get_data():
    """
    Returns two 2D lists of users and books respectively
    """
    # Must be called at the start of the program, program won't work otherwise

    # csv.reader returns a csv.Reader object which is converted to a list so that
    # all list operations can be used to manipulate data
    with open(BOOKS_FILE, "r") as books_f:
        books = list(csv.reader(books_f))

    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    return books, users

def save_books_data(books_data, users_data):
    """
    Writes the data from the 2D lists into the books and users files
    """
    # Must be called at the end of the program after all the changes to the data have been made
    # data won't be saved into the file otherwise
    with open(BOOKS_FILE, "w", newline="") as books_f:
        writer = csv.writer(books_f)
        writer.writerows(books_data)

    with open(USERS_FILE, "w", newline="") as users_f:
        writer = csv.writer(users_f)
        writer.writerows(users_data)

# reset_data_files()
books_data, users_data = get_data()
books_data.append(["Harry Potter", "Fantasy", "12345", "JK. Rowling", "in-shelf"])
save_books_data(books_data, users_data)
