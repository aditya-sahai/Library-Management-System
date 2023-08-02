import os
import csv
from datetime import datetime, date


BOOKS_FILE = os.path.join(os.getcwd(), "books.csv")
USERS_FILE = os.path.join(os.getcwd(), "users.csv")
BOOK_STATUS_FILE = os.path.join(os.getcwd(), "book-status.csv")
LOG_FILE = os.path.join(os.getcwd(), "log.csv")


# READING/WRITING DATA RELATED FUNCTIONS -----------------------------------------------------------
def reset_data_files(reset_books=True, reset_users=True, reset_books_status=True, reset_log=True):
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
            users_f.write("First Name,Last Name,Phone,Membership Date,Duration")
    if reset_books_status:
        with open(BOOK_STATUS_FILE, "w", newline="") as book_status_f:
            book_status_f.write("ISBN,Phone,Duration,Issue Date")
    if reset_log:
        with open(LOG_FILE, "w", newline="") as log_f:
            log_f.write("User Name,Phone,Book Name,ISBN,Duration,Issue Date,Return Date\n")

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

    with open(BOOK_STATUS_FILE, "r", newline="") as book_status_f:
        book_statuses = list(csv.reader(book_status_f))

    return books, users, book_statuses

def save_data(books_data, users_data, book_statuses):
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

    with open(BOOK_STATUS_FILE, "w", newline="") as book_status_f:
        writer = csv.writer(book_status_f)
        writer.writerows(book_statuses)

# --------------------------------------------------------------------------------------------------

# USER RELATED FUNCTIONS ---------------------------------------------------------------------------
def find_user(users_data, phone_num):
    """
    Returns users index in the users_data 2D list
    If user not found, returns None
    Usage:
    if find_user():
        <code block when user found>
    else:
        <display message that user not found>
    """
    for user_num in range(len(users_data)):
        if users_data[user_num][2] == phone_num:
            return user_num 

def add_user(users_data, first_name, last_name, phone_num, duration=30):
    """
    Saves user info in users csv file
    """
    # Called when add new user
    # default duration for membership is 30 days
    date = datetime.now()
    date = f"{date.day}/{date.month}/{date.year}"
    users_data.append([first_name, last_name, phone_num, date, duration])

def renew_user(users_data, phone_num, duration=30):
    """
    Renews the membership date, searches for user using phone number
    """
    # Called when renew user
    phone_num = phone_num.strip()
    user_num = find_user(users_data, phone_num)
    date = datetime.now()
    date = f"{date.day}/{date.month}/{date.year}"
    users_data[user_num][3] = date
    users_data[user_num][4] = duration

def edit_user(users_data, phone_num, new_data):
    """
    Can be used to change the users name and phone number. If value of any key is 'None' that user
    field isn't changed
    new data = {"first-name": abc,"last-name": cde,"phone-num": fgh}
    """
    # Called when edit user
    user_num = find_user(users_data, phone_num)
    if new_data["first-name"] != None:
        users_data[user_num][0] = new_data["first-name"].strip()
    if new_data["last-name"] != None:
        users_data[user_num][1] = new_data["last-name"].strip()
    if new_data["phone-num"] != None:
        users_data[user_num][2] = str(new_data["phone-num"].strip())

# --------------------------------------------------------------------------------------------------

# BOOK RELATED FUNCTIONS ---------------------------------------------------------------------------
def get_shelf(books_data):
    """
    Returns a {"in-shelf": in_shelf,"not-in-shelf": not_in_shelf} where in_shelf/not_in_shelf is a
    list of book names
    Usage: if user_book in books_data["in-shelf"]:
        <code block when book in shelf>
    elif user_book in books_data["not-in-shelf"]:
        <code block when book in shelf>
    else:
        <display message that no such book in library>
    """
    books = {"in-shelf": [], "not-in-shelf": []}
    # looped from [1:] to avoid key error due to book[4] giving 'Status' (col heading)
    for book in books_data[1:]:
        books[book[4]].append(book[0])
        # directly uses book status as a key to append the book[0] (book name) to the required list
    return books

def add_book(books_data, name, isbn, genre, author):
    """
    Adds a book into the library database when the library buys a new book
    """
    # Called when 'add new book'
    books_data.append([name, genre, isbn, author, "in-shelf"])

def issue_book(books_data, book_statuses, phone, isbn, duration=7):
    """
    Changes status of book from 'in-shelf' to 'not-in-shelf' and writes record in book-status.csv
    logging done once book is returned
    """
    # Called when issue book
    isbn = str(isbn).strip()
    for book_num in range(len(books_data)):
        if books_data[book_num][1].strip() == isbn:
            date = datetime.now()
            date = f"{date.day}/{date.month}/{date.year}"
            books_data[book_num][4] = "not-in-shelf"
            book_statuses.append([books_data[book_num][1], phone, duration, date])
            break

def return_book(books_data, users_data, book_statuses, isbn):
    """
    Changes status of book from 'not-in-shelf' to 'in-shelf' and deletes record from book-status.csv
    and logs the data
    """
    # idea for late return: if book returned late then reduce 1 day from duration of user membership
    isbn = isbn.strip()
    for status_num in range(len(book_statuses)):
        if book_statuses[status_num][0].strip() == isbn:
            phone, duration, issue_date = book_statuses[status_num][1:]
            del book_statuses[status_num]
            break

    issue_date_d, issue_date_m, issue_date_y = issue_date.split("/")
    issue_date = date(int(issue_date_y), int(issue_date_m), int(issue_date_d))
    return_date = date.today()

    days_elapsed = (return_date - issue_date).days # to be compared with duration for late return
    issue_date = f"{issue_date.day}/{issue_date.month}/{issue_date.year}"
    return_date = f"{return_date.day}/{return_date.month}/{return_date.year}"

    user_num = find_user(users_data, phone)
    user_name = users_data[user_num][0] + " " + users_data[user_num][1]
    # concatenated first name and last name

    for book_num in range(len(books_data)):
        if books_data[book_num][1].strip() == isbn:
            book_name = books_data[book_num][0].strip()
            books_data[book_num][4] = "in-shelf"
            break

    data_row = [user_name, phone, book_name, isbn, duration, issue_date, return_date]

    with open(LOG_FILE, "a", newline="") as log_f:
        writer = csv.writer(log_f)
        writer.writerow(data_row)

    if days_elapsed > int(duration):
        print("Late")
    else:
        print("On Time")

# --------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    reset_data_files(reset_books=False, reset_users=False, reset_books_status=True, reset_log=True)
    # books_data, users_data, book_statuses = get_data()
    # save_data(books_data, users_data, book_statuses)
