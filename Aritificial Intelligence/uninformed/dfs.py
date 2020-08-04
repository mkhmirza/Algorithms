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


def dfs(graph,source,destination):
    
    stack = [source]
    while stack:
        path = stack.pop()
        # explore last element of the stack
        node = path[-1]
        # print("Node: {}".format(node))
        if node == destination:
            return path # return constructed path
        for n in graph.get(node,[]):
            # add current node to list 
            nPath = list(node)
            # add current node's neighbour into the list 
            nPath.append(n)
            # append new list to stack
            stack.append(nPath)
            
    

# driver code 
if __name__ == "__main__":    
    print("Shortest Path Using Depth-First Search Method")
    print("Shortest Path: {}".format(dfs(graph,"0","2")))