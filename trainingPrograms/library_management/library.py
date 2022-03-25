
from user import Admin,User
from book import Book
class Library():
    def __init__(self):
        self.books=[]
        self.users=[]
        self.admins=[]
        self.shelve=[]

    def add_books(self,book):
        self.books.append(book)
    def add_admins(self,admin):
        self.admins.append(admin)
    def add_users(self,user):
        self.users.append(user)
    def add_shelves(self,shelve):
        self.shelves.append(shelve)
    def book_existance(self,book_name):
        for item in self.books:
            if item.book_name == book_name:
                print(f"{item.book_name} book exists")    
    def display_avaliable_books(self):
            for item in self.books:
                if item.status == "available":
                    print(f"available book:book_id:{item.id}, book_name: {item.book_name}, author: {item.author}, status:{item.status} rack_no:{item.rack_no}")
    
if __name__ =="__main__":
    knl_library=Library()
    book1=Book(1,"aaa","ax","available",1)
    book2=Book(2,"bbb","bx","available",1)
    book3=Book(3,"ccc","cx","available",2)
    admin1=Admin("admin1","1A",415222222,"admin1@gmail.com")
    admin2=Admin("admin2","2A",4152252,"admin2@gmail.com")
    admin1.shelves_manges=[1,2]
    #print(admin1.shelves_manged)
    knl_library.add_books(book1)
    knl_library.add_books(book2)
    knl_library.add_books(book3)
    knl_library.add_admins(admin1)
    knl_library.add_admins(admin2)
    knl_library.display_avaliable_books()

    admin1.issue_book("aaa",knl_library.books)
    knl_library.display_avaliable_books()
    Admin.checked_out_books()
    knl_library.book_existance("ccc")
