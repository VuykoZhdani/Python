from binarytree import binarytree
binarytree
from book import book


def main():
    book1 = book("Wizard", "Lyman", 1901, 200, "chmo")
    book2 = book("Of", "Frank",  1902,100, "chmo")
    book3 = book("OZ", "Baum",  1903,120, "chmo")
    new_binary_tree = binarytree()
    new_binary_tree.insert(book1)
    new_binary_tree.insert(book2)
    new_binary_tree.insert(book3)

    print(new_binary_tree.find_nodes_by_publisher(5))
    new_binary_tree.print_tree()

    new_binary_tree.delete_everyone_with_author(12)
    new_binary_tree.print_tree()

    print(new_binary_tree.insert(book("OZ", "Baum",  1903,120, "chmo")))
if __name__ == '__main__':
    main()