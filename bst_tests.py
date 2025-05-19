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
    
    def test_is_empty(self):
        self.assertEqual(True, is_empty(None))
        self.assertEqual(False, is_empty(BinarySearchTree(2, comes_before, None, None)))
        
    def test_insert(self):
       self.assertEqual(BinarySearchTree(2,comes_before,None,None), insert(BinarySearchTree(2, comes_before, None, None), 3, comes_before))
    #     self.assertEqual(BinTree(2,None,BinTree(7,None,None)),insert(BinTree(2,None,None),BinTree(7,None,None)))
    #     self.assertEqual(BinTree(2, BinTree(-1,None,None),None), insert(BinTree(2,None,None),BinTree(-1,None,None)))
        
    # def test_lookup(self):
    #     self.assertEqual(False,lookup(None,4))
    #     self.assertEqual(False,lookup(BinTree(3,BinTree(4,None,None),BinTree(-1,None,None)),5))
    #     self.assertEqual(True,lookup(BinTree(3,BinTree(4,None,None),BinTree(-1,None,None)),4))
        
    #def test_delete(self):
        #self.assertEqual()
        
        
if __name__ == '__main__':
    unittest.main()
