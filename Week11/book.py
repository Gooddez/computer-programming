class book:
    def __init__(self,title,author,price,keywords):
        self.title = title
        self.author = author
        self.price = price
        self.keywords = keywords
        
    def __str__(self):
        output = f'{self.title} by {self.author}\n'
        str_price = f'Price: {self.price:.2f} baht\n'
        str_keywords = f'Keywords: {sorted([x.capitalize() for x in self.keywords])}'
        return output + str_price + str_keywords