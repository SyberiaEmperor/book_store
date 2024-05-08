# pylint: skip-file
import unittest
from coverage import *

from book import *

class SimpleTest(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(True, True)
   
class BookTests(unittest.TestCase):

    def test_new_book(self):
        book = Book("BookName", "Author", 1999, 100, "Publishing", "Detective")
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

if __name__ == '__main__': # pragma: no cover
    unittest.main()