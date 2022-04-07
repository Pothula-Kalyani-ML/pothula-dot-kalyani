
class User():
    def __init__(self, user_name, user_contact, user_email):
        self.user_name = user_name
        self.user_contact = user_contact
        self.user_email = user_email


class Member(User):
    member_count=1
    total_members=[]
    def __init__(self, user_name, user_contact, user_email):
        super().__init__(user_name, user_contact, user_email)

        self.member_id ='M'+str(Member.member_count)
        self.borrowed_books = []
        Member.total_members.append(self)
        Member.member_count += 1
       
   
    @classmethod
    def check_member_existence(self,member_id,book):
        for item in self.total_members:
            if item.member_id == member_id:
                item.borrowed_books.append(book)
                return True
            else:
                print("not a registered member")

    @classmethod
    def book_return(self,book_name,member_id):
        for item in self.total_members:
                if item.member_id == member_id:
                    for index, borrowed_book in enumerate(item.borrowed_books):
                        if borrowed_book.book_name== book_name:
                            print("returned book",book_name)
                            borrowed_book.status = "available"
                            borrowed_book.member_id = ""
                            book_obj=item.borrowed_books.pop(index)
                            return book_obj

                
           

class Admin(User):
    admin_count=1
    issued_books=[]
    def __init__(self, user_name, user_contact, user_email):
        super(). __init__(user_name, user_contact, user_email)
        self.admin_id="A"+str(Admin.admin_count)
        self.shelves_manged = []
        Admin.admin_count +=1

    
        