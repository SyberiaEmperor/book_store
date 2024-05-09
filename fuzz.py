# pylint: skip-file

from pythonfuzz.main import PythonFuzz
from book import *

@PythonFuzz
def book_fuzzing(buf):
    try:
        string = buf.decode("ascii")
        book = Book(string, string, int(string), int(string), string, string)
    except ValueError:
        pass
    except InvalidBookPrice:
        pass
    except InvalidBookYear:
        pass

@PythonFuzz
def deliver_info_fuzzing(buf):
    try:
        string = buf.decode("ascii")
        date_time = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S.%f')
        di = DeliverInfo(string, date_time, UponReceipt)
    except ValueError:
        pass
    except InvalidDateTime:
        pass

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
    date_time_str = '2024-05-10 08:00:00.0'
    date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    di = DeliverInfo("Address", date_time, UponReceipt)
    bs.deliver(cart,di)
    try:
        id = int(buf.decode("ascii"))
        bs.back(id)
    except ValueError:
        pass
    except InvalidBackId:
        pass   

if __name__ == '__main__':
    book_fuzzing()
