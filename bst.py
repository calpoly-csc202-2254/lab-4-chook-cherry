import sys
import unittest
import random
import time
import matplotlib.pyplot as plt
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

# @dataclass(frozen=True)
# class BinarySearchTree:
#     def comes_before(self, x : Any, y : Any) -> bool:
#         if x > y:
#             return False
#         elif x < y:
#             return True
#         else:
#             return False
#     tree : BinTree

@dataclass(frozen=True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree

def is_empty(bst : BinarySearchTree) -> bool:
   match bst.tree:
         case None:
              return True
         case Node(v, l, r):
              return False
       

def insert(bst: BinarySearchTree, x: Any) -> BinarySearchTree:
    def insert_node(node: Optional[Node]) -> Node:
        match node:
            case None:
                return Node(x, None, None)
            case Node(val, l, r):
                if bst.comes_before(x, val):
                    return Node(val, insert_node(l), r)
                else:
                    return Node(val, l, insert_node(r))
    return BinarySearchTree(bst.comes_before, insert_node(bst.tree))



def lookup(bst: BinarySearchTree, x: Any) -> bool:
    match bst.tree:
        case None:
            return False
        case Node(val, l, r):
            if bst.comes_before(x, val):
                return lookup(BinarySearchTree(bst.comes_before, l), x)
            elif bst.comes_before(val, x):
                return lookup(BinarySearchTree(bst.comes_before, r), x)
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
                    return BinarySearchTree(bst.comes_before, l)
                else:
                    min_of_max = find_min_of_max(bst.tree.right)
                    return BinarySearchTree(bst.comes_before,
                                            Node(min_of_max, l, 
                                                 delete(BinarySearchTree(
                                                     bst.comes_before, r), min_of_max).tree))

def find_min_of_max(node: BinTree) -> Any:
    match node:
        case None:
            return None
        case Node(val, l, right):
            if l is None:
                return val
            else:
                return find_min_of_max(l)           

       
# Benchmark parameters
test_sizes = [10000, 50000, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]  # 100K to 1M

k = 20000  # Number of timed inserts/lookups

def test_bst_performance():
    avg_insert_time = []
    avg_lookup_time = []

    for n in test_sizes:
        total_insert_time = 0.0
        total_lookup_time = 0.0

        # Build tree
        comes_before = lambda x, y: x < y  # Standard numeric ordering
        bst = BinarySearchTree(comes_before, None)

        #test insert
        start_insert = time.perf_counter()
        for val in range(n):
            bst = insert(bst, random.uniform(0,1))
        end_insert = time.perf_counter()
        avg_insert_time.append((end_insert - start_insert)/n)
            
        # Lookup test
        start_lookup = time.perf_counter()
        for val in range(k):
            _ = lookup(bst, random.uniform(0,1))
        end_lookup = time.perf_counter()
        total_lookup_time += (end_lookup - start_lookup)
        avg_lookup_time.append(total_lookup_time/k)


        print(f"n={n:,} | avg insert: {avg_insert_time[-1]:.8f}s | "
        f"avg lookup: {avg_lookup_time[-1]:.8f}s | ")


    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(test_sizes, avg_insert_time, marker='o', label="Insert Time")
    plt.xlabel("Tree Size (n)")
    plt.ylabel("Avg Time per Insert (seconds)")
    plt.title("BST Insert Time vs Tree Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(test_sizes, avg_lookup_time, marker='s', label="Lookup Time")
    plt.xlabel("Tree Size (n)")
    plt.ylabel("Avg Time per Lookup (seconds)")
    plt.title("BST Lookup Time vs Tree Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()