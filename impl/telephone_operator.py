from impl.number_prefix_trie import NumberPrefixTrie


class TelephoneOperator:
    def __init__(self):
        self.trie = NumberPrefixTrie()

    def add_telephone_operator_offer(self, phone_number_prefix, price):
        if isinstance(phone_number_prefix, str) and isinstance(price, float):
            self.trie.insert(phone_number_prefix, price)
        else:
            raise ValueError("A string and integer type should be entered respectively")

    def search_for_cheapest_telephone_operator(self, number):
        return self.trie.search(number)