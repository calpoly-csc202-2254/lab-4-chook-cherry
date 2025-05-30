import sys
import unittest
import random
import time
import matplotlib.pyplot as plt
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

test_bst_performance()

class BSTTests(unittest.TestCase):
    def setUp(self):
        # Standard numeric ordering
        self.numeric = lambda x, y: x < y

        bt1 = Node(0, Node(52, None, None), Node(6, Node(23, None, None), None))
        bt2 = None
        bt3 = Node(13, Node(9, Node(4, None, None), Node(11, None, None)), Node(20, Node(15, None, None), Node(25, None, None)))
        bt4 = Node(13, Node(9, Node(4, None, Node(5, None, None)), Node(11, None, None)), Node(20, Node(15, None, None), Node(25, None, None)))

        self.bst1 = BinarySearchTree(self.numeric, bt1)
        self.bst2 = BinarySearchTree(self.numeric, bt2)
        self.bst3 = BinarySearchTree(self.numeric, bt3)
        self.bst4 = BinarySearchTree(self.numeric, bt4)
        self.bst5 = BinarySearchTree(self.numeric, Node(31, None, None))
        self.bst6 = BinarySearchTree(self.numeric, Node(15, Node(9, Node(4, None, None), Node(11, None, None)), Node(20, None, Node(25, None, None))))

    def test_is_empty(self):
        self.assertTrue(is_empty(self.bst2))
        self.assertFalse(is_empty(self.bst1))

    def test_insert(self):
        self.assertEqual(self.bst4, insert(self.bst3, 5))
        self.assertEqual(self.bst5, insert(self.bst2, 31))

    def test_lookup(self):
        self.assertTrue(lookup(self.bst3, 20))
        self.assertFalse(lookup(self.bst3, 7))
        self.assertTrue(lookup(self.bst4, 13))
        self.assertFalse(lookup(self.bst2, 7))
        self.assertFalse(lookup(self.bst2, 9))

    def test_delete(self):
        self.assertEqual(self.bst3, delete(self.bst4, 5))
        self.assertEqual(self.bst2, delete(self.bst5, 31))
        self.assertEqual(self.bst6, delete(self.bst3, 13))
        self.assertEqual(self.bst3, delete(self.bst3, 31))  # 31 not present

    def test_alphabetic_order(self):
        alpha = lambda a, b: a.lower() < b.lower()
        bst = BinarySearchTree(alpha, None)
        bst = insert(bst, "banana")
        bst = insert(bst, "Apple")
        self.assertTrue(lookup(bst, "apple"))
        self.assertFalse(lookup(bst, "cherry"))

    def test_distance_order(self):
        origin = (0, 0)
        def dist_from_origin(p1, p2):
            return (p1[0]**2 + p1[1]**2) < (p2[0]**2 + p2[1]**2)
        bst = BinarySearchTree(dist_from_origin, None)
        bst = insert(bst, (1, 1))
        bst = insert(bst, (0, 2))
        self.assertTrue(lookup(bst, (1, 1)))
        self.assertFalse(lookup(bst, (3, 4)))


if (__name__ == '__main__'):
    unittest.main()
