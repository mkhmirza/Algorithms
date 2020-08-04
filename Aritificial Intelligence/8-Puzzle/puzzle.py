#!/usr/bin/python env

# implementation of 4 searches 
# BFS, DFS, IDS, Greedy Best First Search

# Q1) What is the current representation of the 8 puzzle problem?
# Intial State = [ 2, 8, 3, 1, 6, 4, 7, 0, 5 ] 

# Q2) What is the goal representation you wish to achieve?
# Goal State = [ 1 ,2, 3, 8 ,0, 4, 7, 6, 5 ]

# Q3) What algorithm you want to use for the search?
# For the following problem Greedy Best First Search is more optimal solution
# because of the less number of nodes discovered  

class Puzzle(object):
    def __init__(self,initial,goal):
        self.initial = initial
        self.goal = goal

    def moveUp(self,initial):
        # copy the given board 
        copyInitial = initial.copy()
        # extract the spaceIndex of element 0
        spaceIndex = copyInitial.index(0)
        # if the current index of 0 is on the these indexes we cannot move up
        if spaceIndex == 0 or spaceIndex == 1 or spaceIndex == 2:
            return copyInitial
        else:
            # move up
            copyInitial[spaceIndex-3], copyInitial[spaceIndex] = copyInitial[spaceIndex], copyInitial[spaceIndex-3]
            return copyInitial

    def moveDown(self,initial):
        # copy the given board 
        copyInitial = initial.copy()
        # extract the spaceIndex of element 0
        spaceIndex = copyInitial.index(0)
        # cannot move further down already at the bottom
        if spaceIndex == 6 or spaceIndex == 7 or spaceIndex == 8:
            return copyInitial
        else:
            # move down 
            copyInitial[spaceIndex+3], copyInitial[spaceIndex] = copyInitial[spaceIndex], copyInitial[spaceIndex+3]
            return copyInitial

    def moveRight(self,initial):
        # copy the given board 
        copyInitial = initial.copy()
        # extract the spaceIndex of element 0
        spaceIndex = copyInitial.index(0)
        # cannot move right
        if spaceIndex == 2 or spaceIndex == 5 or spaceIndex == 8:
            return copyInitial
        else:
            # move right 
            copyInitial[spaceIndex+1], copyInitial[spaceIndex] = copyInitial[spaceIndex], copyInitial[spaceIndex+1]
            return copyInitial

    # helper method to calculate solvability of a puzzle
    def inversions(self,initial):
        totalInv = 0
        for i in range(len(initial)):
            for j in range(i+1, len(initial)):
                if (initial[i] > initial[j]):
                    totalInv += 1
        print("Total Inversions: {}".format(totalInv))
        if (totalInv % 2) == 0:
            return True
        else:
            return False

    def moveLeft(self,initial):
        # copy the given board donot directly change the board
        copyInitial = initial.copy()
        # find index of element 0
        spaceIndex = copyInitial.index(0)
        # if the current index of 0 is on the left hand side of the board 
        if spaceIndex == 0 or spaceIndex == 3 or spaceIndex == 6:
            # return the board unchanged as we cannot move further left 
            return copyInitial
        else:
            # move the elemet 0 to left 
            copyInitial[spaceIndex - 1], copyInitial[spaceIndex] = copyInitial[spaceIndex], copyInitial[spaceIndex-1]
            return copyInitial 

    def bfs(self):
        "Performs a Breath First Search on 8 puzzle problem"
        # init number of discoverd nodes 
        nodesDiscovered = 0
        # init queue with initial state
        queue = [self.initial]
        # init explored nodes with initial
        explored = [self.initial]

        while queue: # queue not empty
            # extract the 1st node as FIFO
            node = queue.pop(0)
            
            # if current extracted node is goal then return the node
            # with number of nodes discovered 
            if node == self.goal:
                return (node,nodesDiscovered)

            # get children or leaf nodes of the current node 
            leafNodes = [self.moveUp(node), self.moveDown(node), self.moveRight(node), self.moveLeft(node)]
            
            # discover node
            nodesDiscovered  += 1
            
            for leaf in leafNodes:
                
                # if the current leaf is not explored already 
                if leaf not in explored:
                    # add it to the queue of explored nodes 
                    explored.append(leaf)
                    # if the leaf node is not the initial node 
                    if leaf != self.initial:
                        # append the current leaf node in to the
                        queue.append(leaf)

    def dfs(self):
        "Performs a Depth First Search on 8 puzzle problem"
        # init number of discoverd nodes 
        nodesDiscovered = 0 
        # init the stack with initial state 
        stack = [self.initial]
        # init explored nodes with initial state
        explored = [self.initial]

        while stack:
            # extract the last element of the stack as LIFO
            node = stack.pop()

            # if current extracted node is goal then return the node
            # with number of nodes discovered 
            if node == self.goal:
                return (node,nodesDiscovered)

            # get children or leaf nodes of the current node 
            leafNodes = [self.moveUp(node), self.moveDown(node), self.moveRight(node), self.moveLeft(node)]
            # discover each leaf node
            nodesDiscovered  += 1
                
            for leaf in leafNodes:
                # if the current leaf is not explored already 
                if leaf not in explored:
                    # add it to the queue of explored nodes 
                    explored.append(leaf)
                    # if the leaf node is not the initial node
                    if (leaf != self.initial):
                        # append the current leaf into the last of the stack     
                        stack.append(leaf)

    # helper function used to calculate misplaced tiles 
    # as hueristic for greedy best first search    
    def getMisplacedTiles(self,node):
        misplacedTiles = 0
        for i in range(0,len(node)):
            if node[i] != self.goal[i]:
                misplacedTiles += 1
        return misplacedTiles

    def greedySearch(self):
        "Performs Greedy Best First Search"

        nodesDiscovered = 0

        # get total misplaced tiles for the initial state 
        initialMisplacedTiles = self.getMisplacedTiles(self.initial)
       
        # init the tuple(state,hueristic) with a queue
        queue = [(self.initial,initialMisplacedTiles)]
       
        # init exlpored nodes 
        explored = [self.initial]
        
        while queue:
            
            # extract the state/node with min hueristic 
            node = min(queue, key = lambda k: k[1])
            elementToPop = queue.index(node)
            queue.pop(elementToPop)

            # if current extracted node is goal then return the node
            # with number of nodes discovered 
            if node[0] == self.goal:
                return (node,nodesDiscovered)

            # get children or leaf nodes of the current node 
            leafNodes = [self.moveUp(node[0]), self.moveDown(node[0]), self.moveRight(node[0]), self.moveLeft(node[0])]

            nodesDiscovered += 1

            for leaf in leafNodes:
    
                # get misplaced tiles as hueristics for each node 
                hueristicEachNode = self.getMisplacedTiles(leaf)
                # if the current leaf is not explored already 
                if leaf not in explored:
                    # add it to the queue of explored nodes 
                    explored.append(leaf)
                    # if the leaf node is not the initial node 
                    if leaf != self.initial:
                        # append the current leaf node in to the
                        queue.append((leaf,hueristicEachNode))

    # searches the tree within the maxdepth
    # depth limit search
    def dls(self,node,maxDepth):
        # reached the end of max depth stop
        # recursiving 
        if maxDepth == 0:        
            if node == self.goal:
                # if the goal state is found return a tuple(boolValue, leafNode)
                return (True, node)
            else:
                return False

        elif maxDepth > 0: 
            # generate 4 leaf nodes by moving up,down, right or left 
            leafNodes = [self.moveUp(node), self.moveDown(node),
            self.moveRight(node), self.moveLeft(node)]
            
            for leaf in leafNodes:
                # recursive call to check if the current leaf is the target and 
                # the max depth hasnt been reached 
                if self.dls(leaf,maxDepth - 1):
                    # return the currnet leaf node being explored
                    return (self.dls(leaf, maxDepth - 1))

            # the target/goal wasnt found within the maxdepth
            return False

    # keep iterating until the target is found or maxdepth is reached
    # iterative deeping search
    def ids(self,maxDepth):
        # make a copy of the original initial state
        node = self.initial.copy()
        # iterating over and over until the maxdepth is not reached
        for i in range(0,maxDepth):
            # this cond is true if we found the goal within the maxdepth 
            if self.dls(node,maxDepth):
                # return goal which was found
                return (self.dls(node,maxDepth))

        #the loop ended as the maxdepth was reached and the goal was not found
        return False


# print algorthms stats using pretty formating 
def printStats(algo,puzzleStart,goalState,goalReceived,nodes = 0):
    "Print the current search stats"

    print(f"{algo}")
    print('-' * 60)
    print(f"Number of Nodes Discovered :  {nodes}")
    print(f"Initial State Given :    {puzzleStart}")
    print(f"Goal State Given    :    {goalState}")
    
    print(f"Goal State Received :    {goalReceived}")
    print('-' * 60)
    print()


# calcualte number of nodes for iddfs using b branching factor
# d as depth limit 
def calculateNodesIddfs(b,d):
    nodes = 0 
    for i in range(0,d+1):
        nodes += (d + 1 - i) * (b**i)
    return nodes 


if __name__ == "__main__":

    puzzleStart  = [ 2, 8, 3, 1, 6, 4, 7, 0, 5 ]
    goalState    = [ 1 ,2, 3, 8 ,0, 4, 7, 6, 5 ]

    
    puzzle = Puzzle(puzzleStart,goalState)
    if puzzle.inversions(puzzleStart):
        print()
        print("Following Choices: ")
        print("1. Breadth First Search")
        print("2. Greedy Best First Search")
        print("3. Depth First Search")
        print("4. Iterative Deepining Depth First Search")
        print()
        choice = int(input("Enter(1-4): "))
        print()
        
        if choice == 1:
            # return (goalNode,nodesDiscovered) 
            rv = puzzle.bfs() 
            printStats("1.Breath First Search",puzzleStart,goalState,rv[0],rv[1])
        elif choice == 2:
            # returns solved state and number of misplace tiles 
            rv = puzzle.greedySearch()
            printStats("2.Greedy Best First Search",puzzleStart,goalState,rv[0],rv[1])
        elif choice == 3:
            print("WARNING: DFS is going to take some time")  
            rv = puzzle.dfs()
            printStats("3.Depth First Search",puzzleStart,goalState,rv[0],rv[1])
        elif choice == 4:
            maxDepth = 5
            rv = puzzle.ids(maxDepth)
            if rv:

                # calcualte number of nodes discovered for iddfs using mathematical 
                # formuala sigma(i=0, d) (5 + 1 - i)*(b^i) where 'b' is branching factor
                # 'd' is max depth limit 
             
                numNodes = calculateNodesIddfs(4, maxDepth) 

                printStats("4.Iterative Deepining Depth First Search ",
                puzzleStart,goalState,rv[1],numNodes)         
                print("Goal was found within the maxdepth")
                print(f"Current Max Depth: {maxDepth}")
                
            else:
                print("Goal was not found within the maxdepth")
        else:
            print("Try Again!")
    else: 
        print("This puzzle cannot be solved..")


