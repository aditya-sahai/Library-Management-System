import os
import csv
from datetime import date, timedelta
from tkinter import messagebox

BASE_DIR = os.getcwd()
BOOKS_FILE = os.path.join(BASE_DIR, "books.csv")
USERS_FILE = os.path.join(BASE_DIR, "users.csv")
BOOK_STATUS_FILE = os.path.join(BASE_DIR, "book-status.csv")
LOG_FILE = os.path.join(BASE_DIR, "log.csv")


def checkphoneformat(libid): # ITS CHECKING LIBRARY ID. Didn't want to change name as then I would have to change it everywhere.
    """
    Simple function that checks if phone number has the correct format or not.
    """
    if len(str(libid))!=7:
        return "length"
    elif str(libid).isnumeric() == False:
        return "datatype"
    else:
        return "correctformat"
    

def checkphoneformat2(phoneno): #THIS ONE IS CHECKING PHONE NO.
    """
    Simple function that checks if phone number has the correct format or not.
    """
    if len(str(phoneno))!=10:
        return "length"
    elif str(phoneno).isnumeric() == False:
        return "datatype"
    else:
        return "correctformat"
    

def generate_id():
    """
    Returns a unique 7 digit user ID for users.csv
    If all possible ids used, returns None
    """
    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    # obtaining a list of user ids already in the database
    user_ids = []
    for user in users[1:]: # sliced to skip through header
        user_ids.append(user[0])

    for user_id in range(1000000, 10000000): # values in range are to iterate through 7 digits nums
        if str(user_id) not in user_ids: # means unique id generated
            return str(user_id)

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
            users_f.write("ID,First Name,Last Name,Phone,Registration Date,Expiry Date\n")
    if reset_books_status:
        with open(BOOK_STATUS_FILE, "w", newline="") as book_status_f:
            book_status_f.write("ISBN,Phone,Issue Date,Expected Return Date\n")
    if reset_log:
        with open(LOG_FILE, "w", newline="") as log_f:
            log_f.write("User ID,User Name,Phone,Book Name,ISBN,Issue Date,Expected Return Date,Actual Return Date\n")

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
    Returns "done" if successful.
    """
    # phone number should be a string without whitespace at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    user_id = generate_id()
    registration_date = date.today()
    expiry_date = registration_date + timedelta(days=duration)

    # changing dates to dd/mm/yy format
    registration_date = registration_date.strftime("%d/%m/%Y")
    expiry_date = expiry_date.strftime("%d/%m/%Y")

    # saving the data if phone no. and name both are unique
    row = [user_id, first_name, last_name, phone, registration_date, expiry_date]
    if checkphoneformat2(phone)=="correctformat":
        with open(USERS_FILE, "a", newline="") as users_f:
            writer = csv.writer(users_f)
            writer.writerow(row)
        return("done", user_id)

def issue_book(isbn, user_id, duration=7):
    """
    Checks if given user id and book exist, if book is "in-shelf" and valid user id then
    issues the book by adding new record to book-status.csv and changing status to "not-in-shelf".
    Returns "id" if user with given user id not found, "isbn" if book with given isbn not
    exists, "expired" if user membership expired, "not-in-shelf" if user id and isbn are valid
    but book is already issued by someone and "done" if issuing book completed successfully.
    """
    # user id and isbn should be strings without whitespace at the ends

    # loading users data and books data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    with open(BOOKS_FILE, "r", newline="") as books_f:
        books = list(csv.reader(books_f))

    # checking if user with given user id exists
    user_found = False
    for user in users:
        if user_id == user[0]:
            user_found = True
            break

    # checking if user membership has expired or not
    d, m, y = user[5].split("/")
    expiry_date = date(int(y), int(m), int(d))
    if expiry_date < date.today(): # true if expired
        return "expired"

    if not user_found:
        return "id"

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

    row = [isbn, user_id, issue_date, expected_return_date]
    with open(BOOK_STATUS_FILE, "a", newline="") as book_status_f:
        writer = csv.writer(book_status_f)
        writer.writerow(row)

    # changing "in-shelf" to "not-in-shelf"
    with open(BOOKS_FILE, "w", newline="") as books_f:
        writer = csv.writer(books_f)
        writer.writerows(books)

    return "done"

def renew_user(user_id, duration=30):
    """
    Returns "id" if user with given user id not found and "done" if membership renewed successfully.
    """
    # user id should be a string without whitespace at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    user_found = False
    for user in users:
        if user_id == user[0]: # user found here
            user_found = True
            registration_date = date.today()
            expiry_date = registration_date + timedelta(days=duration)

            # changing dates to dd/mm/yy format and updating user
            user[4] = registration_date.strftime("%d/%m/%Y")
            user[5] = expiry_date.strftime("%d/%m/%Y")

    if not user_found:
        return "id"

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
        if book_statuses[book_status_num][1] == user[0]: # user found
            if late:
                d, m, y = user[5].split("/")
                user[5] = (date(int(y), int(m), int(d)) - timedelta(days=1)).strftime("%d/%m/%Y")
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
    row = [user[0], user[1].title() + " " + user[2].title(), user[3], book[0], isbn, book_statuses[book_status_num][2], book_statuses[book_status_num][3], actual_return_date]
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

def edit_user(user_id, first_name, last_name, phone, del_acc=False):
    """
    Updates user data in the csv file. Keeps original user data if None passed as argument.
    Returns "id" if user not found and "done" if successful.
    """
    # old_phone must be a string without whitespaces at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    user_found = False
    for user_num in range(len(users)):
        user = users[user_num]
        if user[0] == user_id: # user found
            if del_acc:
                del users[user_num]
            if first_name:
                user[1] = first_name.strip().title()
            if last_name:
                user[2] = last_name.strip().title()
            if phone:
                user[3] = phone.strip()
            user_found = True
            break

    if not user_found:
        return "id"

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

def user_status(user_id):
    """
    Returns (registration_date, expiry_date, is_expired) if user found otherwise returns "id".
    """
    # phone must be a string without whitespaces at the ends

    # loading users data
    with open(USERS_FILE, "r", newline="") as users_f:
        users = list(csv.reader(users_f))

    for user in users:
        if user[0] == user_id:
            rd, rm, ry = user[4].split("/") # registration_date d, m and y respectively
            ed, em, ey = user[5].split("/") # expiry d, m and y respectively
            expiry_date = date(int(ey), int(em), int(ed))
            is_expired = expiry_date < date.today()
            return (user[4], user[5], is_expired)

    return "id"

# reset_data_files(reset_books=False, reset_users=False, reset_books_status=False, reset_log=False)