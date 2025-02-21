class book:
    title = 'title'
    isbn = 'isbn'
    author = 'author'
    publisher = 'publisher'
    price = 0
    def sample(self):
        pass
    def calshipping(self):
        pass

class ebook(book):
    file_size = 0
    print_length = 0
    current_page = 0
    def next(self):
        pass
    def previous(self):
        pass

class audiobook:
    pass

class paperback:
    pass
