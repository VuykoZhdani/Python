from node import node
from book import book


class binarytree:

    def __init__(self):
        self.root = None

    def insert(self, book: book):
        if self.root is None:
            self.root = node(book)
        else:
            current_node = self.root
            while True:
                if book.name < current_node.book.name:
                    if current_node.left is None:
                        current_node.left = node(book)
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node(book)
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right

    def print_tree(self):
        if self.root is None:
            print("U lost ur root")
        else:
            if self.root.right:
                self.root.right.print_nodes()
            if self.root.left:
                self.root.left.print_nodes()
            print(self.root.book)

    def make_to_list(self, node=None, nlist=None):
        if nlist is None:
            nlist = []
        if node is not None:
            nlist.append(node)
            self.make_to_list(node.right, nlist)
            self.make_to_list(node.left, nlist)

    def to_list(self):
        list_of_nodes = []
        if self.root:
            list_of_nodes.append(self.root)
            self.make_to_list(self.root.right, list_of_nodes)
            self.make_to_list(self.root.left, list_of_nodes)
        return list_of_nodes

    def find_nodes_by_publisher(self, publisher):
        list_of_nodes = self.to_list()
        list_of_nodes_with_publisher = []
        for nodes in list_of_nodes:
            if nodes.book.publisher == publisher:
                list_of_nodes_with_publisher.append(nodes)
        return list_of_nodes_with_publisher


    def find_nodes_by_author(self, author):
        list_of_nodes = self.to_list()
        list_of_nodes_with_author = []
        for nodes in list_of_nodes:
            if nodes.book.author == author:
                list_of_nodes_with_author.append(nodes)
        return list_of_nodes_with_author

    def delete_everyone_with_author(self, author: int):
        list_of_group = self.find_nodes_by_author(author)
        for nodes in list_of_group:
            if nodes == self.root:
                if self.root.right is not None:
                    self.root = self.root.right
                else:
                    self.root = self.root.left
            nodes.delete_node()

    def print_publisher_books(self, publisher: int):

        integer = 0
        while True:
            found_book = self.find_by_publisher(publisher - integer)
            if found_book is None:
                break
            else:
                print(found_book.book)
            integer += 1

