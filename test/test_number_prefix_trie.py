import unittest
from impl.number_prefix_trie import NumberPrefixTrie


class TestNumberPrefixTrie(unittest.TestCase):

    def test_insert_operator_offers_and_search(self):
        trie = NumberPrefixTrie()
        trie.insert('467', 5.0)
        trie.insert('46', 0.5)
        trie.insert('1', 0.8)

        self.assertEqual(trie.search('4673212345'), 5.0)
        self.assertEqual(trie.search('46123'), 0.5)
        self.assertEqual(trie.search('1'), 0.8)

        self.assertIsNone(trie.search('44'))
        self.assertIsNone(trie.search('2'))
        self.assertIsNone(trie.search('0'))

    def test_search_empty_trie(self):
        trie = NumberPrefixTrie()

        self.assertIsNone(trie.search('4673212345'))
        self.assertIsNone(trie.search('1'))
        self.assertIsNone(trie.search(''))


if __name__ == '__main__':
    unittest.main()
