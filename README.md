# Telephone calls routing problem solution

This is a solution for determining the cheapest telephone operator for a given phone number based on predefined pricing rules set by different operators.

# Components
CheapestOperatorUtil: Contains a static method to find the cheapest operator among multiple operators for a given telephone number.

Node: Represents a node in the number prefix trie used for efficiently storing and searching telephone number prefixes and their associated prices.

NumberPrefixTrie: A trie data structure used by the telephone operator to store and search for telephone number prefixes along with their respective prices.

TelephoneOperator: Represents a telephone operator entity that uses the number prefix trie to add offers and search for the cheapest price for a given number.
