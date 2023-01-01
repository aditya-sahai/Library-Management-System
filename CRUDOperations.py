import os
import datetime


'''
Buttons hover code
Placing this here because this file is imported almost everywhere,
So its convenient to call this function from here
'''
def button_enterhover(e):
    e.widget['background'] = "#1a1a1a"

def button_leavehover(e):
    e.widget['background'] = 'black'



BOOKS_DATA_DIR = os.path.join(os.getcwd(), "books")

genre_shelf = {
    "sci-fi": 1,
    "fantasy": 2,
    "fiction": 3,
    "drama": 4,
    "educational": 5,
}

status_conversion = {
    "in-shelf": True,
    "not-in-shelf": False,
}

def reset_all_files():
    """
    Removes all the data and creates all the files again.
    """
    for genre in genre_shelf:
        file_path = os.path.join(BOOKS_DATA_DIR, f"shelf-{genre_shelf[genre]}.csv")
        with open(file_path, "w") as f:
            f.write("\"Book Name\",\"ISBN\",\"Author\",\"Status\",\"Issued-By\",\"Issued-On\"\n")

def write_new_record(genre, book_name, isbn, author):
    """
    Writes new entry in the respective file.
    (Called when library gets a new book)
    """
    file_path = os.path.join(BOOKS_DATA_DIR, f"shelf-{genre_shelf[genre]}.csv")
    with open(file_path, "a") as f:
        f.write(f"\"{book_name}\",\"{isbn}\",\"{author}\",\"in-shelf\",\"None\",\"None\"\n")

def get_book_record(genre, req_book_name):
    """
    Returns data of the book from file.
    (Called when admin/user wants to see book data)
    """
    file_path = os.path.join(BOOKS_DATA_DIR, f"shelf-{genre_shelf[genre]}.csv")
    with open(file_path, "r") as f:
        data = f.read()

    for record in data.split("\n")[1:-1]:
        name, isbn, author, status, issued_by, issued_on = record[1:-1].split("\",\"")
        status = status_conversion[status]

        # checks if required book is found
        if name.lower() == req_book_name.lower():
            return {
                "Book Name": name.title(),
                "ISBN": isbn,
                "Author": author.title(),
                "Status": status,
                "Issued By": issued_by,
                "Issued On": issued_on,
            }

    return None

def edit_existing_record(genre, req_book_name, issuer_name=None):
    """
    Used when a person issues a book.
    Returns true if record updated successfully, false if record not found.
    (Called when user issues a book)
    'Puts book back in shelf' if no name is passed, 'issues book' when a name is given.
    If book is already issued by someone and additional name is passed, book will not be issued to
    the new person.
    Returns true if data updated successfully, false if book not found or already issued by someone.
    """
    file_path = os.path.join(BOOKS_DATA_DIR, f"shelf-{genre_shelf[genre]}.csv")
    with open(file_path, "r") as f:
        data = f.read() 

    new_data = ""
    record_found = False
    for record in data.split("\n")[:-1]:
        name, isbn, author, status, issued_by, issued_on = record[1:-1].split("\",\"")

        # checks if required book is found
        if name.lower() == req_book_name.lower():
            # checking if user wants to issue book and if book is in shelf
            # case for book in shelf and user wants to issue
            if issuer_name and status_conversion[status]:
                date = datetime.datetime.now()
                date = f"{date.day}-{date.month}-{date.year}"
                line = f"\"{name}\",\"{isbn}\",\"{author}\",\"not-in-shelf\",\"{issuer_name}\",\"{date}\"\n"
                record_found = True

            # case for book already issued but new user wants to issue
            elif issuer_name and not status_conversion[status]:
                line = record + "\n"

            # case for returning the issued book
            else:
                line = f"\"{name}\",\"{isbn}\",\"{author}\",\"in-shelf\",\"None\",\"None\"\n"
                record_found = True

            new_data += line

        else:
            new_data += record + "\n"

    if record_found:
        with open(file_path, "w") as f:
            f.write(new_data)
        return True

    return False

def delete_existing_record(genre, req_book_name):
    """
    Removes the book record.
    """
    file_path = os.path.join(BOOKS_DATA_DIR, f"shelf-{genre_shelf[genre]}.csv")
    with open(file_path, "r") as f:
        data = f.read() 

    new_data = ""
    record_found = False
    for record in data.split("\n")[:-1]:
        name, isbn, author, status, issued_by, issued_on = record[1:-1].split("\",\"")

        # checks if required book is found
        if name.lower() == req_book_name.lower():
            record_found = True

        else:
            new_data += record + "\n"

    if record_found:
        with open(file_path, "w") as f:
            f.write(new_data)
        return True

    return False


if __name__ == "__main__":
    reset_all_files()
    # write_new_record("sci-fi", "interstellar", 1111111, "someone else")
    # print(get_book_record("sci-fi", "interstellar"))
    # print(edit_existing_record("sci-fi", "interstellar"))
    # print(delete_existing_record("sci-fi", "interstellar"))