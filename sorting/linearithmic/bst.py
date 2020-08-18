#!/usr/python/env

# binary search tree for tree sort algorith

from node import Node

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def returnNode(self, value: int) -> Node:
        """
        Returns a Node object of value(int)
        """
        return Node(value)

    def Insert(self, value):
        """
        Inserts new node given as a value(int) in the bst 
        """
        node = self.returnNode(value)
        y = None 
        x = self.root
        while x != None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        elif node.value > y.value:
            y.right = node

    
    def printInOrderWalking(self):
        self.__inOrderWalking(self.root)

    def __inOrderWalking(self, node):
        """
        Performs in order traversal on the tree
        """
        if node != None:
            self.__inOrderWalking(node.left)
            print(f"Node :{node.value}")
            self.__inOrderWalking(node.right)


    def Build(self, data: list):
        """
        Builds a bst from data(list)
        """
        self.root = Node(data[0])
        for i in range(1,len(data)):
            
            valueOfNode = data[i]        
            self.Insert(valueOfNode)

