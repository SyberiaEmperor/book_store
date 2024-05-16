
class Cart:
    def __init__(self):
        self.list = set()

    def add_book(self, ident):
        self.list.add(ident)

    def get_list(self):
        return list(self.list)
