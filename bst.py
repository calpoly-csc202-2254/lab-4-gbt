from ast import Call
import sys
import unittest
from typing import * 
from dataclasses import dataclass
sys.setrecursionlimit(10**6)


def example_fun(x : int) -> bool:
    return x < 142

BinTree : TypeAlias = Union["BinarySearchTree", None]

        
#determines if one value comes before another        
def comes_before(a, b) -> bool: #boolean
    if a < b:
        return True
    else:
        return False
    

@dataclass (frozen=True)
class BinarySearchTree:
    value: Any
    comes_before: Callable[[Any, Any], bool] #takes two type Anys, returns bool
    left: BinTree
    right: BinTree
#a
# Given a BinarySearchTree, return True if tree is empty, False otherwise
def is_empty(l: BinTree) -> bool:
    match l:
        case None:
            return True
        case BinarySearchTree(v, _, left, right):
            return False

# Adds value to tree by using comes_before function to determine which path to take @ each node, 
# inserts into left subtree if value comese before value stores, right subtree otherwise
def helper(i: BinTree, new_value: Any, comes_before) -> BinTree:
    match i:
        case None:
            return BinarySearchTree(new_value, comes_before, None, None)
        case BinarySearchTree(value, comes_before, left, right):
            if comes_before(new_value, value) is True:
                return BinarySearchTree(value, comes_before, helper(left, new_value, comes_before), right)
            else:
                return BinarySearchTree(value, comes_before, left, helper(right, new_value, comes_before))

def insert(l: BinTree, val: Any, comes_before) -> BinTree:
    return helper(l, val, comes_before)

# Returns True if value is stored in tree and False if else
#Instead, you will use the comes_before function to determine if the value appears in the tree. 
# More specifically, when comparing two values, if neither value "comes before" the other, 
# then the values will be considered equal (i.e., for our purposes, (not (a < b) and not (b < a)) -> a = b).
def lookup(i: BinTree, look: Any, comes_before) -> bool:
    match i:
        case None:
            return False
        case BinarySearchTree(value, comes_before, left, right):
            if comes_before(look, value) is True:
                return True
            else:
                if left == None and right == None:
                    return False
                else:
                    return lookup(left,look,comes_before) or lookup(right,look,comes_before)
                   

# Removes value from tree (if there) while preserving binary search tree property for given node's value, 
# if many nodes containing values need to be removed, only one such node will be removed
def delete():
    pass

