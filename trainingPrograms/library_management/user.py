class User():
    def __init__(self, user_name, user_id, user_contact, user_email):
        self.name = user_name
        self.id = user_id
        self.contact = user_contact
        self.email = user_email


class member(User):
    pass


class Admin(User):
    issued_books = []

    def __init___(self, user_name, user_id, user_contact, user_email):
        self.shelves_manged = []
        User. __init__(self, user_name, user_id, user_contact, user_email)

    def issue_book(self, book_name, books):
        for item in books:
            if item.book_name == book_name:
                self.issued_books.append(item)
                item.status = "taken"
                print(item.id)
                print(item.status)

    @classmethod
    def checked_out_books(self):
        for item in self.issued_books:
            print(
                f"checked out book:book_id:{item.id}, book_name: {item.book_name}, author: {item.author}, status:{item.status} rack_no:{item.rack_no}")
