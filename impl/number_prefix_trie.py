from impl.node import Node


class NumberPrefixTrie:
    def __init__(self):
        self.root = Node()

    def insert(self, prefix, price):
        node = self.root
        for digit in prefix:
            if digit not in node.children:
                node.children[digit] = Node()
            node = node.children[digit]
        node.price = price

    def search(self, number):
        node = self.root
        lowest_price = None

        for digit in number:
            if digit in node.children:
                node = node.children[digit]
                if node.price is not None:
                    lowest_price = node.price
            else:
                break

        return lowest_price
