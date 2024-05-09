
from book import Book
from deliver_info import DeliverInfo
from cart import Cart

class BookStore:
    
    def __init__(self):
        self.counter = 0
        self.tokey = {}
        self.fromkey = {}
        self.given = set()
    
    def add_book(self, book: Book):
        if book in self.tokey:
            return self.tokey[book]
        self.tokey[book] = self.counter
        self.fromkey[self.counter] = book
        self.counter += 1
        return self.counter - 1
        
    def get(self, ind):
        if ind in self.given:
            return None
        if ind in self.fromkey:
            return self.fromkey[ind]
        return None
        
    def deliver(self, cart: Cart, info: DeliverInfo):
        print(info)
        book_list = cart.get_list()
        for book_id in book_list:
            if not self.get(book_id) is None:
                self.given.add(book_id)
                
    def back_book(self, ind):
        if not ind in self.given:
            raise InvalidBackId
        self.given.remove(ind)
        
    
class InvalidBackId(Exception):
    pass
