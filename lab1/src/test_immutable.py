import unittest
from immutable import *


class MyTestCase(unittest.TestCase):
    def test_size(self):
        t = ImHashTable(11)
        self.assertEqual(t.size, 11)

    def test_itm_size(self):
        ht = ImHashTable()
        ht.list_to_hashTable([1, 2, 4, 5, 10, 20, 45])
        self.assertEqual(ht.itm_size(), 7)

    def test_hash(self):
        self.assertEqual(ImHashTable().hash(10), 0)
        self.assertEqual(ImHashTable().hash(15), 5)

    def test_hashTable_to_list(self):
        ht1 = ImHashTable()
        ht1.list_to_hashTable([3, 5, 28, 90, 34])
        self.assertEqual(ht1.hashTable_to_list(), [90, 3, 34, 5, 28])

    def test_list_to_hashTable(self):
        lists = [3, 5, 48, 39]
        ht2 = ImHashTable()
        ht2.list_to_hashTable(lists)
        self.assertEqual(ht2.hashTable_to_list(), lists)

    def test_insert(self):
        t = ImHashTable(10, [12])
        self.assertEqual(t.insert(2), t)

    def test_delete(self):
        t = ImHashTable(10, [18, 28,58,68, 38])
        self.assertEqual(t.delete(18).hashTable_to_list(), [18, 28,58,68, 38])
        self.assertEqual(t.delete(38).hashTable_to_list(), [18, 28,58,68, 38])
        self.assertEqual(t.delete(58).hashTable_to_list(), [18, 28,58,68, 38])

    def test_mconcat(self):
        t = ImHashTable(10, [1, 3, 5, 10])
        t2 = HashTable(10, [1, 4, 9])
        self.assertEqual(t.mconcat(t2).hashTable_to_list(), [10, 1, 3, 5])

    def test_reduce(self):
        # sum of empty list
        lst = ImHashTable(0)
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 0)
        # sum of list
        lst = ImHashTable(10 , [1, 2, 3])
        self.assertEqual(lst.reduce(lambda st, e: st + e, 0), 6)
        # size
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            lst = ImHashTable(10, e)
            self.assertEqual(lst.reduce(lambda st, _: st + 1, 0), lst.itm_size())

    def test_map(self):
        lst = ImHashTable(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        lst.map(str)
        self.assertEqual(lst.hashTable_to_list(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_find(self):
        t = ImHashTable()
        t.list_to_hashTable([10, 3, 51])
        self.assertEqual(t.find(10), True)
        self.assertEqual(t.find(5), False)


if __name__ == '__main__':
    unittest.main()