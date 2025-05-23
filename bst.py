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
        match node:
            case None:
                return Node(x, None, None)
            case Node(val, left, right):
                if bst.comes_before(x, val):
                    return Node(val, insert_node(left, x), right)
                else:
                    return Node(val, left, insert_node(right, x))

    return BinarySearchTree(insert_node(bst.tree, x))


def lookup(bst: BinarySearchTree, x: Any) -> bool:
    match bst.tree:
        case None:
            return False
        case Node(val, left, right):
            if bst.comes_before(x, val):
                return lookup(BinarySearchTree(left), x)
            elif bst.comes_before(val, x):
                return lookup(BinarySearchTree(right), x)
            else:
                return True

            

       

