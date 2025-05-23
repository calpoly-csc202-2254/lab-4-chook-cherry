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

class BSTTests(unittest.TestCase):
    def test_is_empty(self):
        self.assertEqual(True, is_empty(bst2))
        self.assertEqual(False, is_empty(bst1))

    def test_insert(self):
        self.assertEqual(bst4, insert(bst3, 5))
        self.assertEqual(bst5, insert(bst2, 31))

if (__name__ == '__main__'):
    unittest.main()
