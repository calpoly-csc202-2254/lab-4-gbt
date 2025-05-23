from ast import Call
import sys
import unittest
from typing import *
from dataclasses import dataclass
import time

sys.setrecursionlimit(10 ** 6)


def example_fun(x: int) -> bool:
    return x < 142




BinTree: TypeAlias = Union["BinarySearchTree", None]


# determines if one value comes before another
def comes_before(a, b) -> bool:  # boolean
    if a < b:
        return True
    else:
        return False


@dataclass(frozen=True)
class BinarySearchTree:
    value: Any
    comes_before: Callable[[Any, Any], bool]  # takes two type Anys, returns bool
    left: BinTree
    right: BinTree


# Given a BinarySearchTree, return True if tree is empty, False otherwise
def is_empty(l: BinTree) -> bool:
    match l:
        case None:
            return True
        case BinarySearchTree(v, _, left, right):
            return False
    return None

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
    return None

def insert(l: BinTree, val: Any, comes_before) -> BinTree:
    return helper(l, val, comes_before)

# Returns True if value is stored in tree and False if else
# Instead, you will use the comes_before function to determine if the value appears in the tree.
# More specifically, when comparing two values, if neither value "comes before" the other,
# then the values will be considered equal (i.e., for our purposes, (not (a < b) and not (b < a)) -> a = b).
def lookup(i: BinTree, look: Any, comes_before) -> bool:
    match i:
        case None:
            return False
        case BinarySearchTree(value, comes_before, left, right):
            if comes_before(look, value) is False and comes_before(value, look) is False:
                return True
            else:
                if left is None and right is None:
                    return False
                else:
                    return lookup(left, look, comes_before) or lookup(right, look, comes_before)
    return None

# Removes value from tree (if there) while preserving binary search tree property for given node's value
# Values in left subtree come before
# If many nodes containing values need to be removed, only one such node will be removed
def find_min_val(n: BinarySearchTree):  # Helper function for delete function #changed n to pass BinarySearchTree
    if n.left is None:  # Base case
        return n.value
    return find_min_val(n.left)


def delete(n: BinTree, del_val: Any, comes_before) -> BinTree:  # a and b for left and right subtrees (?)
    if n is None:
        return None

    go_left = comes_before(del_val, n.value)

    if go_left:
        return BinarySearchTree(n.value, comes_before, delete(n.left, del_val, comes_before), n.right)
    elif del_val == n.value:
        # Case 1: no children
        if n.left is None and n.right is None:
            return None

        # Case 2: only left child
        if n.right is None:
            return n.left

        # Case 3: only right child
        if n.left is None:
            return n.right

        # Case 4: two children
        new_value = find_min_val(n.right)
        return BinarySearchTree(new_value, comes_before, n.left, delete(n.right, new_value, comes_before))
    else:
        return BinarySearchTree(n.value, comes_before, n.left, delete(n.right, del_val, comes_before))



if __name__ ==  "__main__":
    l = BinarySearchTree(2, comes_before, None, None)
    start_time = time.perf_counter()
    result = is_empty(l)
    end_time = time.perf_counter()
    test1 = end_time - start_time
    print(test1)


    l1 = BinarySearchTree(2,comes_before,None,None)
    start_time = time.perf_counter()
    result = insert(l1, 7, comes_before )
    end_time = time.perf_counter()
    test2 = end_time - start_time
    print(test2)