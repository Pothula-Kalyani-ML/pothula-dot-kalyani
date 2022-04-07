
from shelves import Shelves
from user import*
from book import Book
class Library():
    
    def __init__(self):
        self.books=[]
        self.members=[]
        self.admins=[]
        self.shelves=[]
        self.checked_out_book=[]
    

    def add_books(self,book,shelf_id):

        Shelves.add_books_to_shelf(book,shelf_id)
        self.books.append(book)

        self.sort_books()

    def sort_books(self):
        index=len(self.books)-1
        while index>0 and (self.books[index].book_name < self.books[index-1].book_name):
            self.books[index], self.books[index-1]=self.books[index-1], self.books[index]
            index -= 1 


    def return_a_book(self,book_name,member_id,shelf_id):
        book_obj=Member.book_return(book_name,member_id)
        Shelves.add_books_to_shelf(book_obj,shelf_id)      
                
    def add_admins(self,admin):
        self.admins.append(admin)


    def add_member(self):
        self.members=Member.total_members
    

    def add_shelves(self):
        self.shelves=Shelves.total_shelves

        
    def display_avaliable_books(self):
            for item in self.books:
                if item.status == "available":
                    print(f"available book:book_id:{item.id}, book_name: {item.book_name}, author: {item.author}, status:{item.status} shelf_id:{item.shelf_id}")
    

    def check_availabilty_and_issue_a_book(self,book_name,mem_id):
        for book in self.books:
            if book.book_name == book_name:
                print("book exists")
                if book.status=="available":
                    print("book available to issue")
                    if Member.check_member_existence(mem_id,book):
                        book.status = "checked_out"
                        book.member_id = mem_id
                        shelf_id=book.shelf_id
                        position=book.book_position
                        print(f"present in : {shelf_id} at position {position}")
                        Shelves.remove_book_to_issue(position,shelf_id,book)
                        
                        print(f"present in : {book.shelf_id} at position{book.book_position}")
                        break
                else: print("book_checked out")
            elif book.book_name > book_name:
                print(f"{book_name} book does not exists in library")
                break           
      


if __name__ =="__main__":
    knl_library=Library()
    shelf1=Shelves("shelf1",3)
    shelf2=Shelves("shelf2",2)
    shelf3=Shelves("shelf3",10)

    knl_library.add_shelves()

    
    book1=Book("aaa","ax")
    book2=Book("bbb","bx")
    book3=Book("ccc","cx")
    book4=Book("a2","azx")
    

    admin1=Admin("admin1",415222222,"admin1@gmail.com")
    admin2=Admin("admin2",4152252,"admin2@gmail.com")
    
    member1=Member("mem1",987,"mem1@gmail.com")
    member2=Member("mem2",564,"mem2@gmail.com")

    knl_library.add_member()
    knl_library.add_books(book1,"s1")
    knl_library.add_books(book2,"s1")
    knl_library.add_books(book3,"s1")
    knl_library.add_books(book4,"s3")



    print("books in shelf1",shelf1.shelf_books)

    #knl_library.check_availabilty_and_issue_a_book("aaa","M1")
    print("books in shelf1",shelf1.shelf_books)

    knl_library.check_availabilty_and_issue_a_book("bbb","M1")
    knl_library.check_availabilty_and_issue_a_book("a2","M2")
    knl_library.display_avaliable_books()

    knl_library.return_a_book("bbb","M1","S3")
    knl_library.display_avaliable_books()

    

    print("books in shelf1",shelf1.shelf_books)

    print("brrowed_book by{}:{}".format(member1.member_id,member1.borrowed_books))
    print("books in shelf1",shelf1.shelf_books)
    knl_library.check_availabilty_and_issue_a_book("a2","M1")

    

