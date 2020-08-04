#!/usr/bin/python env
graph = { 
          "0" : [ "1",  "5"],
          "1" : [ "2",  "3"],
          "2" : [          ],
          "3" : [ "2" , "4"],
          "4" : [          ],
          "5" : [ "6" , "7"],
          "6" : [    "7"   ],
          "7" : [          ] 
}


def bfs(graph,source,destination):
    
    queue = [source]
    while queue:
        path = queue.pop(0)
        # explore last element of the queue
        node = path[-1]
        # print("Node: {}".format(node))
        if node == destination:
            return path # return constructed path
        for n in graph.get(node,[]):
            # add current node to list 
            nPath = list(node)
            # add current node's neighbour into the list 
            nPath.append(n)
            # append new list to queue
            queue.append(nPath)
            
    

# driver code 
if __name__ == "__main__":    
    print("Shortest Path Using Breadth-First Search Method")
    print("Shortest Path: {}".format(bfs(graph,"0","2")))