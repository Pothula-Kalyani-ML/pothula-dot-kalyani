
from turtle import position


class Shelves():
    total_shelves=[]
    shelves_count=1
    def __init__(self,shelf_name,shelf_size):
        self.shelf_name=shelf_name
        self.shelf_id="s"+str(Shelves.shelves_count)
        self.shelf_books=[]
        self.shelf_size=shelf_size
        self.space_left_in_shelf=shelf_size
        self.book_position=0
        Shelves.total_shelves.append(self)
        Shelves.shelves_count += 1
    @classmethod
    def available_shelves(self):
        print(self.total_shelves)


    @classmethod
    def add_books_to_shelf(self,book,shelf_id):
        for item in self.total_shelves:
            if shelf_id == item.shelf_id: 
                if item.space_left_in_shelf:
                    item.shelf_books.append(book)
                    book.shelf_id=shelf_id
                    book.book_position=item.book_position
                    item.space_left_in_shelf -= 1
                    item.book_position += 1
                else:
                    print(f"to add {book.book_name} to shlef,{shelf_id}  is full")
    @classmethod               
    def remove_book_to_issue(self,position,shelf_id,book):
        for item in self.total_shelves:
            if shelf_id == item.shelf_id: 
                item.shelf_books.pop(position)
                book.shelf_id=""
                book.book_position= -1
                item.space_left_in_shelf += 1
                for index,shelf_book in enumerate(item.shelf_books):
                    if index>position-1:
                        shelf_book.book_position -= 1
