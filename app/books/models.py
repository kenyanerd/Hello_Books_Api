# a list of all the books
books = []

class Book:
    '''class containing all the books '''

    def __init__(self):
        self.id = None
        self.title = None
        self.description = None
        self.category = None
        self.author = None
        self.copies_available = None
        self.available = True

    #a method to add a book
    def save(self):
        books.append(self)

    #a method to remove a book
    def remove(self):
        books.remove(self)

    @staticmethod
    def get_book_by_id(bk_id):
        for book in books:
            if book.id == bk_id:
                return books
            else:
                pass
        return None

    @staticmethod
    def get_all_books():
        return books







