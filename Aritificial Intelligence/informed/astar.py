#!/usr/bin/python env

import sys

# note: the following representation of 'Traveling in Romania' is represented by 
# Adj matrix which is a Sparse matrix since number of zeros are greater than the size 
# This not a very good representation beacuse of the sparsity of the graph but i just find it easy :p

class Graph(object):
    def __init__(self,hueristic,graph):
        self.hueristic = hueristic
        self.graph = graph


    def getNeighbours(self,node):
        neighbours = []
        # get current node from tuple 
        currentNode = node[0]
        #print("Current Node: {}".format(currentNode))
        for i in range(0,len(self.hueristic)):
            if self.graph[currentNode][i] > 0:
                neighbours.append((i,self.graph[currentNode][i]))

        return neighbours

    def printGraphNodes(self):
        # each city name is shortened to its initial and is represent by 
        # an integer in the graph for the matrix 
        initialsCitiesInRomania = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Z']
        for i in range(0,len(self.graph)):
            print("{}.{} - {}".format(i,initialsCitiesInRomania[i],self.hueristic[i]))


    def bfs(self,source,dest):

        print()

        # adding self.hueristic for source
        self.hueristic[source] = self.hueristic[source] + 0
        queue = [(source,0,self.hueristic[source])]

        # queue = [(source,path-distance,self.hueristic)]
        # minValue = min(queue, key = key = lambda t: t[2])
        visited = [False] * (len(self.graph))
        # visited the source only
        visited[source]= True

        # init distances as max size 
        distance = [sys.maxsize] * (len(self.graph))
        distance[source] = 0

        # track previous nodes
        prev = {source: None}

        while queue:
            print()
            print(queue)
            # get min value tuple from the queue based on the (path-cost + self.hueristic-value) 
            v = min(queue, key = lambda t: t[2]) # 0 -> node 1 -> path-distance 2 -> self.hueristic 
            # pop the currently extracted element from the queue
            elementToPop = queue.index(v)
            queue.pop(elementToPop)

            # check for the destination after dequeuing poping the node
            if v[0] == dest:
                print("Goal Reached..")
                print(prev) 
                sys.exit()

            #explore last element of the queue
            eachNeighbour = self.getNeighbours(v)
            # get only the nodes from tuple
            currentNodeNeighbours = [x[0] for x in eachNeighbour]
            
            # get neighbours weights from the tuple 
            currentNodeNeighboursWeight = [x[1] for x in eachNeighbour]
            # current node which is extracted from the node 
            currentNode = v[0]
            print("Node {} Neigbours: {}".format(currentNode,currentNodeNeighbours))
            for n in currentNodeNeighbours:
                if not visited[n]:
                    # mark as visited 
                    visited[n] = True
                    prev[n] = currentNode
                    # weigh for current node 
                    weight = self.graph[n][currentNode]    # weigh = graph[1][0]
                    # calculate distance 
                    if distance[n] > (distance[currentNode] + weight):
                        distance[n] = distance[currentNode] + weight
                    # append neigbour node 'n' and its weight 'weight' into the queue

                    # add weight + previous self.hueristic value to new priority for self.hueristic value 
                    newHueristicValue = weight + self.hueristic[n]
                    print("Current Nodes {} : {} + {}  = {}".format(n,weight,self.hueristic[n],newHueristicValue))
                    
                    # cannot do this only check when dequening 
                    # if n == dest:
                    #     print("Goal Reached..")
                    #     print(prev) 
                    #     sys.exit()
                    
                    queue.append((n,weight,newHueristicValue))
            

if __name__ == "__main__":


    graph = [[0, 0, 0,   0, 0,   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 140, 118, 0, 0, 75],      
            [0, 0, 0,   0, 0, 211, 90, 0, 0, 0, 0, 0, 0, 101, 0, 0, 0, 85, 0, 0 ],      
            [0, 0, 0, 120, 0,   0, 0, 0, 0, 0, 0, 0, 0, 138, 146, 0, 0, 0, 0, 0 ],       
            [0, 0, 120, 0, 0, 0, 0, 0,   0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0    ],      
            [0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0        ],      
            [0, 211, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0      ],       
            [0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0        ],      
            [0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 0, 0       ],      
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 92, 0       ],       
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 111, 0, 0, 0      ],      
            [0, 0, 0, 75, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0       ],      
            [0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0        ],      
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 151, 0, 0, 0, 71      ],       
            [0, 101, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0, 0, 0, 0    ],      
            [0, 0, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0, 80, 0, 0, 0, 0     ],      
            [140, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 151, 0, 80, 0, 0, 0, 0, 0   ],     
            [118, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0     ],      
            [0, 85, 0, 0, 0, 0, 0, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 0     ],      
            [0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 0, 0, 0, 0, 0, 0, 0, 142, 0, 0      ],     
            [75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 0, 0, 0, 0, 0, 0, 0       ]]     
                    


    hueristic = [366,0,160,242,161,176,77,151,226,244,241,234,380,100,193,253,329,80,199,374]

   
    g = Graph(hueristic,graph)    
    g.printGraphNodes()
    g.bfs(0,1)

   