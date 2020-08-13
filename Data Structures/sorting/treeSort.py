#!/usr/bin/python env

from bst import BinarySearchTree

bst = BinarySearchTree()
data = [5,6,3,1,2,4]
# build bst from data
bst.Build(data)
# sort data using in order traversal
bst.printInOrderWalking()


