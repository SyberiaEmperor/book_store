
class Book:
    def __init__(self, name: str, author: str, year: int, price: int, publisher: str, genre: str):
        if year < 0:
            raise InvalidBookYear
        if price < 0:
            raise InvalidBookPrice
        self.name = name
        self.author = author
        self.pub_year = year
        self.price = price
        self.publisher = publisher
        self.genre = genre

class InvalidBookYear(Exception):
    pass

class InvalidBookPrice(Exception):
    pass
