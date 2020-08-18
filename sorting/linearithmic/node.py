#!/usr/python env

# class to represent node in bst
class Node(object):
    def __init__(self, value):
        # value of the node 
        self.value = value
        # left child of the current node
        self.left = None
        # right child of the current node 
        self.right = None
        # parent node of current node
        self.parent = None
