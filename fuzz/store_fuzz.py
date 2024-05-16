# pylint: skip-file

from pythonfuzz.main import PythonFuzz
from datetime import *

import os, sys
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]))

from book import *
from cart import *
from deliver_info import *
from book_store import *

@PythonFuzz
def book_store_fuzzing(buf):
    bs = BookStore()
    book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
    bs.add_book(book)
    book = Book("BookName2", "Author2", 2000, 100, "Publishing", "Detective")
    bs.add_book(book)
    book = Book("BookName3", "Author3", 2015, 100, "Publishing", "Detective")
    bs.add_book(book)
    book = Book("BookName4", "Author4", 1999, 120, "Publishing", "Detective")
    bs.add_book(book)
    book = Book("BookName5", "Author5", 1999, 140, "Publishing", "Detective")
    bs.add_book(book)
    cart = Cart()
    cart.add_book(0)
    cart.add_book(1)
    date_time = datetime.now() + timedelta(days=1)
    di = DeliverInfo("Address", date_time, Pay.UPON_RECEIPT)
    bs.deliver(cart,di)
    try:
        id = int(buf.decode("ascii"))
        string = buf.decode("ascii")
        book = Book(string, string, int(string), int(string), string, string)
        ti = bs.add_book(book)
        cart.add_book(ti)
        bs.deliver(cart, di)
        bs.back_book(id)
    except ValueError:
        pass
    except InvalidBackId:
        pass   
    
if __name__ == '__main__':
    book_store_fuzzing()
