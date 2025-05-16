import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)


def example_fun(x : int) -> bool:
    return x < 142

BinTree : TypeAlias = Union["Node" : Any, None]

@dataclass (frozen=True)
class BinarySearchTree:
    def comes_before(listy):
        listy = []
        return listy - 1
#a
    # Given a BinarySearchTree, return True if tree is empty, False otherwise
    def is_empty(self) -> bool:
        e = len(listy)
        match e:
            case 0:
                return True
            case :
                return False

    # Adds value to tree by using comes_before function to determine which path to take @ each node, inserts into left subtree if value comese before value stores, right subtree otherwise
    def insert():

    # Returns True if value is stored in tree and False if else
    def lookup():

    # Removes value from tree (if there) while preserving binary search tree property for given node's value, if many nodes containing values need to be removed, only one such node will be removed
    def delete():
