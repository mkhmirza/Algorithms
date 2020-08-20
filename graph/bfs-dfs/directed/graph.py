#!/usr/bin/python env

# representation of a undirected graph 

class Graph(object):
    def __init__(self, nodes):
        # no of nodes 
        self.nodes = nodes 
        self.matrix = [[0 for x in range(nodes)] for y in range(nodes)]

    def addNode(self, u, v):
        self.matrix[u][v] = 1

    def printMatrix(self):
        print(" --- Graph Matrix --- ")
        for i in range(0, self.nodes):
            for j in range(0, self.nodes):
                print(f"{self.matrix[i][j]}", end=' ')
            print()
        print()
        
    def getNeighbor(self, node):
        neighbor = []
        for i in range(0, self.nodes):
            if self.matrix[node][i] > 0:
                neighbor.append(i)
        return neighbor

    def getNumberNodes(self):
        return self.nodes