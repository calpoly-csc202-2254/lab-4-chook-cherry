import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

def main():
    return


BinTree : TypeAlias = Union[None, "Node"]

@dataclass(frozen=True)
class Node :
    val : Any
    left : BinTree
    right : BinTree


# Examples:
bt1 : BinTree = Node(0, Node(52, None, None), Node(6, Node(23, None, None), None))
bt2 : BinTree = None

@dataclass(frozen=True)
class BinarySearchTree:
    def comes_before(self, x : Any, y : Any) -> bool:
        if x > y:
            return False
        elif x < y:
            return True
        else:
            return False
    tree : BinTree

def is_empty(bst : BinarySearchTree) -> bool:
   match bst.tree:
         case None:
              return True
         case Node(v, l, r):
              return False
       

def insert(bst: BinarySearchTree, x: Any) -> BinarySearchTree:
    def insert_node(node: Optional[Node], x: Any) -> Node:
        if node is None:
            return Node(x, None, None)
        if bst.comes_before(x, node.val):
            return Node(node.val, insert_node(node.left, x), node.right)
        else:
            return Node(node.val, node.left, insert_node(node.right, x))

    return BinarySearchTree(insert_node(bst.tree, x))

            

       

