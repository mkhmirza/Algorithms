#!/usr/bin/python env

# note: this is my own source code for tic tac toe 
# minimax algorithm 


class Game(object):
    def __init__(self,hPlayer,aPlayer):
        # human player 
        self.hPlayer = hPlayer
        # computer player 
        self.aPlayer = aPlayer
        self.board  = [[ '.' for i in range(0,3)] for j in range(0,3)]
 

    def printBoard(self):
        print()
        # top numbering of board 
        for i in range(0,3): print("  | {} |".format(i+1),end =' ')
        print()
        
        for i in range(0,3):
            # side numbering of the board
            print("{}".format(i+1),end='')
            for j in range(0,3):
                print(" | {} | ".format(self.board[i][j]),end=' ')
            print()
        print()



    # get playerX and playerY coordinates
    def getUserXYCoord(self):
        badInput = True
        while badInput:
            # enter human player's x and y coordinates ie 1,2
            x, y = input("Enter x & y coordinates(enter in this format:(x,y): ").split(',') 
            x = int(x)
            y = int(y)
            if (x < 0 or y < 0) or (x > 3 or y > 3):
                print("Invalid input! Please Enter Again!")
                continue
            else:
                badInput = False     
        return int(x) - 1,int(y) - 1 
    # place the current player's move 
    def placeVal(self,currentPlayerX, currentPlayerY,currentPlayer):
    
        if self.board[currentPlayerX][currentPlayerY] == '.':
            self.board[currentPlayerX][currentPlayerY] = currentPlayer
            return 0 # val was placed 
        return -1 # place was not empty  

    def playComputerMove(self,currentPlayer):
        # get best score and playerX and playerY moves 
        (score,playerX,playerY) = self.max()
        print("PlayerX: {} PlayerY: {}".format(playerX+1,playerY+1))
        # place value on the board of the current player
        self.placeVal(playerX,playerY,currentPlayer)
        # check if current moves wins the game
        winner = self.checkWinner()
        # return if there was any winner 
        return winner


    def playHumanMove(self,currentPlayer):

        # place value on the board of the current player     
        rv = -1
        while rv == -1:
            #get human player x,y coordinates
            playerX, playerY = self.getUserXYCoord() 
            
            rv = self.placeVal(playerX,playerY,currentPlayer)
            if rv == -1:
                print("The place was already taken! Please choose a empty space!")
                print()
                continue
            else: 
                print("PlayerX: {} PlayerY: {}".format(playerX+1,playerY+1))   


        # check if the current move wins the game 
        winner = self.checkWinner()
        # return if there was a winner 
        return winner


    def playGame(self):
        print()
        print("Welcome to Tic Tac Toe!")
        print("Human Player:    {}".format(self.hPlayer))
        print("Computer Player: {}".format(self.aPlayer))
        print()       
       
        moves = 0

        # human player goes first, if you want computer to go first then
        currentPlayer = self.aPlayer
        # uncomment above line and comment below line 
        #currentPlayer = self.hPlayer    
        while True:
            
            self.printBoard()

            # change current player 
            if currentPlayer == self.hPlayer:
                
                print(" ** Human Player's Move ** ")
                # play human move, and get winner if there is any        
                winner = self.playHumanMove(currentPlayer)
                # change current player to computer player 
                currentPlayer = self.aPlayer
            else: 
                print(" ** Computer's Move ** ")
                # play computer's move, and get winner if there is any        
                winner = self.playComputerMove(currentPlayer)
                # change current player to human player 
                currentPlayer = self.hPlayer

            # there are places left on the board, we continue playing 
            if winner == None:
                continue
            else: # there was a winner 
                print("Game Over! {} won the game".format(winner))
                self.printBoard() # show final form of the board 
                break # exit the game 

    def checkWinner(self):
        # checking rows if current player won 
        for i in range(0,3):
            if self.board[i][0] != '.' and self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2]:
                return self.board[i][0]

        # checking cols if current player won
        for i in range(0,3):
            if self.board[0][i] != '.' and self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i]:
                return self.board[0][i]
                
        # main diagonal        
        if self.board[0][0] != '.' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
                return self.board[0][0]
                

        # secondary diag
        if self.board[0][2] != '.' and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            return self.board[0][2]
                

        # check to see if the board is full or not 
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.board[i][j] == '.'):
                    return None

        # tie game 
        return 0

    def max(self):

        # scores to track
        # +1 if computer won
        # -1 if computer lost 
        #  0 if result is a tie game 

        currentMaxValue = -2

        # when the method is called currently their is no playerX,playerY
        playerX, playerY = None, None 
        # check winner if current player is winning 
        result = self.checkWinner()
        # self.debug("Current Winner: {}".format(result))
        if result == 'X': # human player won
            return (-1,0,0) # return min value         
        elif result == 'O': # computer player won
            return (1,0,0) # return max value 
        elif result == 0: # game was a tie 
            return (0,0,0) 

        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '.':
                    # set value for computer 
                    self.board[i][j] = 'O' 
                    # calculate if it returns the max values
                    (m,x,y) = self.min()
                    # self.debug("Max Value: ({},{},{})".format(m,maxX,maxY))
                    # check for any value returned by recursing which is greater than
                    # currently set max value
                    if m > currentMaxValue:
                        currentMaxValue = m
                        playerX = i
                        playerY = j
                    # remove the placed marker 
                    self.board[i][j] = '.'
        return (currentMaxValue,playerX,playerY)

    def min(self):
        #scores to track
        # +1 if computer won
        # -1 if human won 
        #  0 if result is a tie game 
        currentMaxValue = 2

        #when the method is called currently their is no playerX,playerY
        playerX, playerY = None, None 
        # check winner if current player is winning 
        result = self.checkWinner()
        # human player won 
        if result == 'X':
            return (-1,0,0)
        elif result == 'O': # computer player won
            return (1,0,0)
        elif result == 0: # the game was a tie 
            return (0,0,0)

        # check the board 
        for i in range(0,3):
            for j in  range(0,3):
                if self.board[i][j] == '.':
                    self.board[i][j] = 'X'
                    (m,x,y) = self.max()
                    if m < currentMaxValue:
                        currentMaxValue = m
                        playerX = i
                        playerY = j
                    self.board[i][j] = '.'

        return (currentMaxValue,playerX,playerY)

if __name__ == "__main__":
    game = Game('X','O')
    game.playGame()    




