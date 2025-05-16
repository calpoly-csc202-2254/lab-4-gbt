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
    
    def test_is_empty(self):
        self.assertEqual(True, is_empty(None))
        self.assertEqual(False, is_empty(BinTree(2,None,None)))
        
    def test_insert(self):
        self.assertEqual(BinTree(2,None,None),insert(None, BinTree(2,None,None)))
        self.assertEqual(BinTree(2,None,BinTree(7,None,None)),insert(BinTree(2,None,None),BinTree(7,None,None)))
        self.assertEqual(BinTree(2, BinTree(-1,None,None),None), insert(BinTree(2,None,None),BinTree(-1,None,None)))
        
    def test_lookup(self):
        self.assertEqual(False,lookup(None,4))
        self.assertEqual(False,lookup(BinTree(3,BinTree(4,None,None),BinTree(-1,None,None)),5))
        self.assertEqual(True,lookup(BinTree(3,BinTree(4,None,None),BinTree(-1,None,None)),4))
        
    def test_delete(self):
        self.assertEqual()
        
        
if (__name__ == '__main__'):
    unittest.main()
