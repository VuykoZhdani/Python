class book:

    def __init__(self, name: str, author: str,year : int, price: int, publisher: str):
        self.name =name
        self.author = author
        self.year = year
        self.price = price
        self.publisher = publisher

    def __str__(self):
        return f"{self.name} {self.author} {self.year}  {self.price}  {self.publisher} "
