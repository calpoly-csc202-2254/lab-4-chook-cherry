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
            case Node(val, l, r):
                if bst.comes_before(x, val):
                    return Node(val, insert_node(l, x), r)
                else:
                    return Node(val, l, insert_node(r, x))

    return BinarySearchTree(insert_node(bst.tree, x))


def lookup(bst: BinarySearchTree, x: Any) -> bool:
    match bst.tree:
        case None:
            return False
        case Node(val, l, r):
            if bst.comes_before(x, val):
                return lookup(BinarySearchTree(l), x)
            elif bst.comes_before(val, x):
                return lookup(BinarySearchTree(r), x)
            else:
                return True
            
def delete(bst: BinarySearchTree, x: Any) -> BinarySearchTree:
    match bst.tree:
        case None:
            return bst
        case Node(val, l, r):
            if bst.comes_before(x, val):
                return BinarySearchTree(Node(val, delete(BinarySearchTree(l), x).tree, r))
            elif bst.comes_before(val, x):
                return BinarySearchTree(Node(val, l, delete(BinarySearchTree(r), x).tree))
            else:
                if l is None:
                    return BinarySearchTree(r)
                elif r is None:
                    return BinarySearchTree(l)
                else:
                    min_of_max = find_min_of_max(bst.tree.right)
                    return BinarySearchTree(Node(min_of_max, l, delete(BinarySearchTree(r), min_of_max).tree))

def find_min_of_max(node: BinTree) -> Any:
    match node:
        case None:
            return None
        case Node(val, l, right):
            if l is None:
                return val
            else:
                return find_min_of_max(l)           

       

