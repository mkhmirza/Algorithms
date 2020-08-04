#!/usr/bin/python env

import sys
graph = [[0, 146, 140, 0, 0, 0, 0, 404],  # 'A' 0
         [146, 0, 151, 0, 0, 0, 0, 0  ],  # 'B' 1
         [140, 151, 0, 99, 0, 0, 80, 0],  # 'C' 2
         [0, 0, 99, 0, 211, 0, 0, 0   ],  # 'D' 3
         [0, 0, 0, 211, 0, 101, 0, 0  ],  # 'E' 4
         [0, 0, 0, 0, 101, 0, 97, 138 ],  # 'F' 5
         [0, 0, 80, 0, 0, 97, 0, 146  ],  # 'G' 6
         [404, 0, 0, 0, 0, 138, 146, 0]]  # 'H' 7

def getNeighbours(node):
    neighbours = []
    # get current node from tuple 
    currentNode = node[0]
    #print("Current Node: {}".format(currentNode))
    for i in range(0,8):
        if graph[currentNode][i] > 0:
            neighbours.append((i,graph[currentNode][i]))

    return neighbours

def bfs(graph,source,destination):

    queue = [(source,0)]
    visited = [False] * (len(graph))
    # visited the source only
    visited[source]= True

    # init distances as max size 
    distance = [sys.maxsize] * (len(graph))
    distance[source] = 0

    while queue:
        # get min value tuple from the queue based on the min distance 
        v = min(queue, key = lambda t: t[1])
        # pop the currently extracted element from the queue
        elementToPop = queue.index(v)
        queue.pop(elementToPop)

    
        #explore last element of the queue
        eachNeighbour = getNeighbours(v)
        # get only the nodes from tuple
        currentNodeNeighbours = [x[0] for x in eachNeighbour]
        # get neighbours weights from the tuple 
        currentNodeNeighboursWeight = [x[1] for x in eachNeighbour]
        # current node which is extracted from the node 
        currentNode = v[0]
        for n in currentNodeNeighbours:
            if not visited[n]:
                # mark as visited 
                visited[n] = True
                # weigh for current node 
                weight = graph[n][currentNode]
                # calculate distance 
                if distance[n] > (distance[currentNode] + weight):
                    distance[n] = distance[currentNode] + weight
                # append neigbour node 'n' and its weight 'weight' into the queue
                queue.append((n,weight))
    return distance 

if __name__ == "__main__":

    source = 0
    print(bfs(graph,0,4))