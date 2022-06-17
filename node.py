from book import book


class node:

    def __init__(self, book: book):
        self.right = None
        self.left = None
        self.parent = None
        self.book = book

    def find_node_by_publisher(self, publisher: str):
        if publisher < self.book.publisher and self.left:
            assert isinstance(self.left.find_node_by_publisher)
            return self.left.find_node_by_publisher(publisher)
        if publisher > self.book.publisher and self.right:
            return self.right.find_node_by_publisher(publisher)
        if publisher == self.book.publisher:
            return self
        return None
    def delete_node(self):
        if self.right is None and self.left is None:
            if self.parent.right is self:
                self.parent.right = None
            if self.parent.left is self:
                self.parent.left = None
        elif self.left is None:
            self.right.parent = self.parent
            if self.parent.right is self:
                self.parent.right = self.right
            if self.parent.left is self:
                self.parent.left = self.right
        elif self.right is None:
            self.left.parent = self.parent
            if self.parent.right is self:
                self.parent.right = self.left
            if self.parent.left is self:
                self.parent.left = self.left
            return self

            self.right.parent = self.parent
            if self.parent is not None:
                if self.parent.right is self:
                    self.parent.right = self.right
                if self.parent.left is self:
                    self.parent.left = self.right
        del self

    def print_nodes(self):
        if self.right:
            self.right.print_nodes()
        if self.left:
            self.left.print_nodes()
        print(self.book)