class Book():
    total_book_count=0
    
    def __init__(self,book_name,book_author):
        self.id="B"+str(Book.total_book_count)
        self.book_name=book_name
        self.author=book_author
        self.status="available"
        self.shelf_id=""
        self.book_position=-1
    
        Book.total_book_count+=1
    