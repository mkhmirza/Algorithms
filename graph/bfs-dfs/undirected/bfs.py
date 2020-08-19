#!/usr/bin/python env

from graph import Graph

def bfs(source):
    # visited 
    visited = [False] * graph.getNumberNodes()

    # init queue using source 
    queue = [source]
    # visited source node 
    visited[source] = True
    
    while(queue):
        # pop first element as FIFO
        node = queue.pop(0)
        print(f"Node: {node}")

        neighbors = graph.getNeighbor(node)
        for n in neighbors:
            if visited[n] != True:
                visited[n] = True
                queue.append(n)

graph = Graph(5)
graph.addNode(0, 4)
graph.addNode(0, 1)

graph.addNode(1, 3)
graph.addNode(1, 4)
graph.addNode(3, 2)
graph.addNode(1, 2)

graph.printMatrix()

print(" --- Breadth First Search ---")
bfs(0)