import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

# Examples:
bt1 : BinTree = Node(0, Node(52, None, None), Node(6, Node(23, None, None), None))
bt2 : BinTree = None
bst1 : BinarySearchTree = BinarySearchTree(bt1)
bst2 : BinarySearchTree = BinarySearchTree(bt2)

bt3 : BinTree = Node(13, Node(9, Node(4, None, None), Node(11, None, None)), Node(20, Node(15, None, None), Node(25, None, None)))
bt4 : BinTree = Node(13, Node(9, Node(4, None, Node(5, None, None)), Node(11, None, None)), Node(20, Node(15, None, None), Node(25, None, None)))
bst3 : BinarySearchTree = BinarySearchTree(bt3)
bst4 : BinarySearchTree = BinarySearchTree(bt4)
bst5 : BinarySearchTree = BinarySearchTree(Node(31, None, None))
bst6 : BinarySearchTree = BinarySearchTree(Node(15, Node(9, Node(4, None, None), Node(11, None, None)), Node(20, None, Node(25, None, None))))

class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(True, is_empty(bst2))
        self.assertEqual(False, is_empty(bst1))

    def test_insert(self):
        self.assertEqual(bst4, insert(bst3, 5))
        self.assertEqual(bst5, insert(bst2, 31))

    def test_lookup(self):
        self.assertEqual(True, lookup(bst3, 20))
        self.assertEqual(False, lookup(bst3, 7))
        self.assertEqual(True, lookup(bst4, 13))
        self.assertEqual(False, lookup(bst2, 7))
        self.assertEqual(False, lookup(bst2, 9))
 
    def test_delete(self):
        self.assertEqual(bst3, delete(bst4, 5))
        self.assertEqual(bst2, delete(bst5, 31))
        self.assertEqual(bst6, delete(bst3, 13))
        self.assertEqual(bst3, delete(bst3, 31))


if (__name__ == '__main__'):
    unittest.main()
