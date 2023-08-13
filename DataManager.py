import os
import csv
from datetime import date, timedelta
from tkinter import messagebox

BASE_DIR = os.getcwd()
BOOKS_FILE = os.path.join(BASE_DIR, "books.csv")
USERS_FILE = os.path.join(BASE_DIR, "users.csv")
BOOK_STATUS_FILE = os.path.join(BASE_DIR, "book-status.csv")
LOG_FILE = os.path.join(BASE_DIR, "log.csv")

def checkphoneformat(phoneno):
    """
    Simple function that checks if phone number has the correct format or not.
    """
    if len(str(phoneno))!=10:
        return "length"
    elif str(phoneno).isnumeric() == False:
        return "datatype"
    else:
        return "correctformat"
    
def openlog():
    """
    Simple function to open log file
    """
    2
    
def reset_data_files(reset_books=True, reset_users=True, reset_books_status=True, reset_log=True):
    """
    Removes all the data from specified files
    """
    # NOT USED IN PROGRAM, MADE ONLY FOR CONVENIENCE WHILE DEVELOPING
    if reset_books:
        with open(BOOKS_FILE, "w", newline="") as books_f:
            books_f.write("Book Name,Genre,ISBN,Author,Status\n")
    if reset_users:
        with open(USERS_FILE, "w", newline="") as users_f:
            users_f.write("First Name,Last Name,Phone,Registration Date,Expiry Date\n")
    if reset_books_status:
        with open(BOOK_STATUS_FILE, "w", newline="") as book_status_f:
            book_status_f.write("ISBN,Phone,Issue Date,Expected Return Date\n")
    if reset_log:
        with open(LOG_FILE, "w", newline="") as log_f:
            log_f.write("User Name,Phone,Book Name,ISBN,Issue Date,Expected Return Date,Actual Return Date\n")

def add_new_book(name, genre, isbn, author):
    """
    Returns "name" if book with given name already exists, "isbn" if book with given isbn already
    exists and returns "done" if new book data given.
    """
    # isbn should be a string without whitespace at the ends

    # loading books data
    with open(BOOKS_FILE, "r", newline="") as books_f:
        books = list(csv.reader(books_f))

    # checking for overlapping data
    for book in books:
        if name.lower() == book[0].lower():
            return "name"
        elif isbn == book[2]:
            return "isbn"

    # saving the data if isbn and name both are unique
    row = [name, genre, isbn, author, "in-shelf"]
    with open(BOOKS_FILE, "a", newline="") as books_f:
        writer = csv.writer(books_f)
        writer.writerow(row)

    return "done"

def add_new_user(first_name, last_name, phone, duration=30):
    """
    Returns "phone" if user with given phone number already exists and returns "done" if phone
    number is unique.
    """
    # phone number should be a string without whitespace at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    # checking for overlapping data
    for user in users:
        if phone == user[2]:
            return "phone"

    registration_date = date.today()
    expiry_date = registration_date + timedelta(days=duration)

    # changing dates to dd/mm/yy format
    registration_date = registration_date.strftime("%d/%m/%Y")
    expiry_date = expiry_date.strftime("%d/%m/%Y")

    # saving the data if phone no. and name both are unique
    row = [first_name, last_name, phone, registration_date, expiry_date]
    if checkphoneformat(phone)=="correctformat":
        with open(USERS_FILE, "a", newline="") as users_f:
            writer = csv.writer(users_f)
            writer.writerow(row)
        return "done"

def issue_book(isbn, phone, duration=7):
    """
    Checks if given phone number and book exist, if book is "in-shelf" and valid phone number then
    issues the book by adding new record to book-status.csv and changing status to "not-in-shelf".
    Returns "phone" if user with given phone number not found, "isbn" if book with given isbn not
    exists, "expired" if user membership expired, "not-in-shelf" if phone number and isbn are valid
    but book is already issued by someone and "done" if issuing book completed successfully.
    """
    # phone number and isbn should be strings without whitespace at the ends

    # loading users data and books data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    with open(BOOKS_FILE, "r", newline="") as books_f:
        books = list(csv.reader(books_f))

    # checking if user with given phone number exists
    user_found = False
    for user in users:
        if phone == user[2]:
            user_found = True
            break

    # checking if user membership has expired or not
    d, m, y = user[4].split("/")
    expiry_date = date(int(y), int(m), int(d))
    if expiry_date < date.today(): # true if expired
        return "expired"

    if not user_found:
        return "phone"

    # checking if book with given isbn exists, if it exists then checking if book is "in-shelf"
    book_found = False
    for book in books:
        if isbn == book[2]:
            book_found = True
            if book[4] == "not-in-shelf":
                return "not-in-shelf"
            else:
                book[4] = "not-in-shelf" # change status to "not-in-shelf" if book is "in-shelf"

    if not book_found:
        return "isbn"

    # writing record in book-status.csv
    issue_date = date.today()
    expected_return_date = issue_date + timedelta(days=duration)

    # changing dates to dd/mm/yy format
    issue_date = issue_date.strftime("%d/%m/%Y")
    expected_return_date = expected_return_date.strftime("%d/%m/%Y")

    row = [isbn, phone, issue_date, expected_return_date]
    with open(BOOK_STATUS_FILE, "a", newline="") as book_status_f:
        writer = csv.writer(book_status_f)
        writer.writerow(row)

    # changing "in-shelf" to "not-in-shelf"
    with open(BOOKS_FILE, "w", newline="") as books_f:
        writer = csv.writer(books_f)
        writer.writerows(books)

    return "done"

def renew_user(phone, duration=30):
    """
    Returns "phone" if user with given phone number not found and "done" if membership renewed
    successfully.
    """
    # phone number should be a string without whitespace at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    user_found = False
    for user in users:
        if phone == user[2] and checkphoneformat(phone)=="correctformat": # user found here
            user_found = True
            registration_date = date.today()
            expiry_date = registration_date + timedelta(days=duration)

            # changing dates to dd/mm/yy format and updating user
            user[3] = registration_date.strftime("%d/%m/%Y")
            user[4] = expiry_date.strftime("%d/%m/%Y")

    if not user_found:
        return "phone"

    # saving changes
    with open(USERS_FILE, "w", newline="") as users_f:
        writer = csv.writer(users_f)
        writer.writerows(users)

    return "done"

def return_book(isbn):
    """
    Uses book-status.csv to check is book is issued, if given book is issued then deletes record
    from book-status.csv and changes "not-in-shelf" to "in-shelf". If book returned after expected
    return date then 1 day subtracted from users membership. Writes record in log.csv
    Returns "not-found" if if no such book issued found (or if book not issued by anyone), "done-l" if process completed successfully
    but late return and returns "done" if book returned on time.
    """
    # isbn must be a string without whitespaces at the ends

    # loading book statuses data, users data amd books data
    with open(BOOK_STATUS_FILE, "r", newline="") as book_status_f:
        book_statuses = list(csv.reader(book_status_f))

    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    with open(BOOKS_FILE, "r", newline="") as books_f:
        books = list(csv.reader(books_f))

    book_is_issued = False
    for book_status_num in range(len(book_statuses)):
        if book_statuses[book_status_num][0] == isbn: # is true if book is issued
            book_is_issued = True
            break

    if not book_is_issued:
        return "not-found"

    d, m, y = book_statuses[book_status_num][3].split("/")
    expected_return_date = date(int(y), int(m), int(d))
    actual_return_date = date.today()
    late = expected_return_date < actual_return_date # true if book returned late
    actual_return_date = actual_return_date.strftime("%d/%m/%Y")

    for user in users:
        if book_statuses[book_status_num][1] == user[2]: # user found
            if late:
                d, m, y = user[4].split("/")
                user[4] = (date(int(y), int(m), int(d)) - timedelta(days=1)).strftime("%d/%m/%Y")
                # reduced one day from membership in the above line
                # saving user changes
                with open(USERS_FILE, "w", newline="") as users_f:
                    writer = csv.writer(users_f)
                    writer.writerows(users)
            break

    # changing from "not-in-shelf" to "in-shelf"
    for book in books:
        if book[2] == isbn:
            book[4] = "in-shelf"
            break

    # logging
    row = [user[0].title() + " " + user[1].title(), user[2], book[0], isbn, book_statuses[book_status_num][2], book_statuses[book_status_num][3], actual_return_date]
    with open(LOG_FILE, "a", newline="") as log_f:
        writer = csv.writer(log_f)
        writer.writerow(row)

    del book_statuses[book_status_num] # removed record

    # saving changes
    with open(BOOK_STATUS_FILE, "w", newline="") as book_status_f:
        writer = csv.writer(book_status_f)
        writer.writerows(book_statuses)

    with open(BOOKS_FILE, "w", newline="") as books_f:
        writer = csv.writer(books_f)
        writer.writerows(books)

    if late:
        return "done-l"
    return "done"

def edit_user(old_phone, first_name, last_name, new_phone):
    """
    Updates user data in the csv file. Keeps original user data if None passed as argument.
    Returns "phone" if user not found and "done" if successful.
    """
    # old_phone must be a string without whitespaces at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    user_found = False
    for user in users:
        if user[2] == old_phone and checkphoneformat(old_phone)=="correctformat": # user found
            if first_name:
                user[0] = first_name.strip().title()
            if last_name:
                user[1] = last_name.strip().title()
            if new_phone:
                user[2] = new_phone.strip()
            user_found = True
            break

    if not user_found:
        return "phone"

    # saving changes
    with open(USERS_FILE, "w", newline="") as users_f:
        writer = csv.writer(users_f)
        writer.writerows(users)

    return "done"

def book_status(isbn):
    """
    Returns "in-shelf" or "not-in-shelf" if book exists and "isbn" if book not found.
    """
    # isbn must be string without whitespaces at the ends

    # loading books data
    with open(BOOKS_FILE, "r", newline="") as books_f:
        books = list(csv.reader(books_f))

    for book in books:
        if book[2] == isbn:
            return book[4]

    return "isbn"

def user_status(phone):
    """
    Returns (registration_date, expiry_date, is_expired) if user found otherwise returns "phone".
    """
    # phone must be a string without whitespaces at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    for user in users:
        if user[2] == phone:
            rd, rm, ry = user[3].split("/") # registration_date d, m and y respectively
            ed, em, ey = user[4].split("/") # expiry d, m and y respectively
            expiry_date = date(int(ey), int(em), int(ed))
            is_expired = expiry_date < date.today()
            return (user[3], user[4], is_expired)

    return "phone"

# reset_data_files(reset_books=False, reset_users=False, reset_books_status=False, reset_log=False)
