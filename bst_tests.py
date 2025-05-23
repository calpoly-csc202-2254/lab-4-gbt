import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *

class BSTTests(unittest.TestCase):
    def test_example_fun(self):
        self.assertEqual(True, example_fun(34))
        self.assertEqual(False,example_fun(1423))
        
    def test_comes_before(self):
        self.assertEqual(True, comes_before(2, 6))
        self.assertEqual(False,comes_before(5,-5))
        self.assertEqual(True, comes_before("abc", "bcd"))
        self.assertEqual(False, comes_before(3.547, 2.345))
    
    def test_is_empty(self):
        self.assertEqual(True, is_empty(None))
        self.assertEqual(False, is_empty(BinarySearchTree(2, comes_before, None, None)))
        self.assertEqual(False, is_empty(BinarySearchTree("abc",comes_before,None,None)))
        
    def test_insert(self):
       self.assertEqual(BinarySearchTree(2,comes_before,None,None), insert(None, 2, comes_before))
       self.assertEqual(BinarySearchTree(2,comes_before, None,BinarySearchTree(7,comes_before,None,None)),insert(BinarySearchTree(2,comes_before,None,None),7,comes_before))
       self.assertEqual(BinarySearchTree(2,comes_before, BinarySearchTree(-1,comes_before,None,None),None), insert(BinarySearchTree(2,comes_before,None,None),-1,comes_before))
       self.assertEqual(BinarySearchTree("fun", comes_before, BinarySearchTree("abc",comes_before,None,None),None), insert(BinarySearchTree("fun",comes_before, None,None),"abc",comes_before))
        
    def test_lookup(self):
        self.assertEqual(False,lookup(None,4,comes_before))
        self.assertEqual(False,lookup(BinarySearchTree(3,comes_before, BinarySearchTree(4,comes_before,None,None),BinarySearchTree(-1,comes_before,None,None)),5,comes_before))
        self.assertEqual(True,lookup(BinarySearchTree(3,comes_before,BinarySearchTree(4,comes_before,None,None),BinarySearchTree(-1,comes_before,None,None)),4,comes_before))
        self.assertEqual(True,lookup(BinarySearchTree("fun", comes_before, BinarySearchTree("abc",comes_before,None,None),None),"abc",comes_before))
        
    def test_delete(self):
         self.assertEqual(None, delete(None,1,comes_before))
         self.assertEqual(None, delete(BinarySearchTree(1,comes_before,None,None),1,comes_before))
         self.assertEqual(BinarySearchTree(1,comes_before,None,None),delete(BinarySearchTree(1,comes_before,None,None),3,comes_before))
         self.assertEqual(BinarySearchTree(6,comes_before,None,None),delete(BinarySearchTree(2,comes_before,None,BinarySearchTree(6,comes_before,None,None)),2,comes_before))
         self.assertEqual(BinarySearchTree("abc",comes_before,None,None),delete(BinarySearchTree("fun", comes_before, BinarySearchTree("abc",comes_before,None,None),None),"fun",comes_before))
        
        
if __name__ == '__main__':
    unittest.main()
