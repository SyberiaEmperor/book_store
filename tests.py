# pylint: skip-file
import unittest
import datetime
from coverage import *

from book import *

class SimpleTest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(True, True)
   
class BookTests(unittest.TestCase):

    def test_new_book(self):
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
        self.assertIsNotNone(book)
        self.assertEqual(book.name, "BookName")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.pub_year, 1999)
        self.assertEqual(book.price, 100)
        self.assertEqual(book.publisher, "Publishing")
        self.assertEqual(book.genre, "Detective")
     
    def test_new_book_bad_year(self):
        self.assertRaises(InvalidBookYear, Book, "BookName", "Author", -56834, 100, "Publishing", "Detective")
   
    def test_new_book_bad_price(self):
        self.assertRaises(InvalidBookPrice, Book, "BookName", "Author", 1997, -68, "Publishing", "Detective")

class CartTests(unittest.TestCase):
    
    def test_new_cart(self):
        cart = Cart()
        self.assertIsNotNone(cart)
    
    def test_cart_add(self):
        cart = Cart()
        cart.add_book(1)
        cart.add_book(2)
        cart.add_book(3)
        self.assertEqual(cart.get_list(), [1,2,3])

class DeliverInfoTests(unittest.TestCase):
    
    def test_new_deliver_info(self):
        date_time_str = '2024-05-10 08:00:00.0'
        date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        di = DeliverInfo("Address", date_time, UponReceipt)
        self.assertIsNotNone(di)
        
    def test_new_bad_deliver_info(self):
        date_time_str = '1999-05-10 08:00:00.0'
        date_time = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        self.assertRaises(InvalidDateTime, DeliverInfo,"Address", date_time, UponOrder)

class BookStoreTests(unittest.TestCase):
    
    def test_new_book_store(self):
        bs = BookStore()
        self.assertIsNotNone(bs)
        
    def test_book_store_add(self):
        bs = BookStore()
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
        id = bs.add_book(book)
        self.assertEqual(id,0)
        book2 = bs.get(id)
        self.assertIsNotNone(book2)
        self.assertEqual(book2.name, book.name)
        
    def test_book_store_bad_add(self):
        bs = BookStore()
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
        id = bs.add_book(book)
        self.assertEqual(id,0)
        book2 = bs.get(id + 1)
        self.assertIsNone(book2)
        
    def test_book_store_deliver(self):
        bs = BookStore()
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
        id = bs.add_book(book)
        cart = Cart()
        cart.add_book(id)
        bs.deliver(cart, deliver_info)
        self.assertIsNone(bs.get(id))
        
    def test_book_store_back(self):
        bs = BookStore()
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
        id = bs.add_book(book)
        cart = Cart()
        cart.add_book(id)
        bs.deliver(cart, deliver_info)
        bs.back_book(id)
        self.assertIsNotNone(bs.get(id))
        
    def test_book_store_bad_back(self):
        bs = BookStore()
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
        id = bs.add_book(book)
        cart = Cart()
        cart.add_book(id)
        bs.deliver(cart, deliver_info)
        self.assertRaises(InvalidBackId, bs.back_book, id+1)

if __name__ == '__main__': # pragma: no cover
    unittest.main()