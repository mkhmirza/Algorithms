#!/usr/bin/python env

from graph import Graph

def dfs(source):
    # visited 
    visited = [False] * graph.getNumberNodes()

    # init stack using source 
    stack = [source]
    # visited source node 
    visited[source] = True
    
    while(stack):
        # pop last element as LIFO
        node = stack.pop()
        print(f"Node: {node}")

        neighbors = graph.getNeighbor(node)
        for n in neighbors:
            if visited[n] != True:
                visited[n] = True
                stack.append(n)

graph = Graph(5)
graph.addNode(0, 4)
graph.addNode(0, 1)

graph.addNode(1, 3)
graph.addNode(1, 4)
graph.addNode(3, 2)
graph.addNode(1, 2)

graph.printMatrix()

print(" --- Depth First Search ---")
dfs(0)