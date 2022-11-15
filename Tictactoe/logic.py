# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
from termcolor import colored, cprint
import time
import random
def DisplayBoard(board):
    
    cprint("*TICTACTOE BOARD*",'magenta')
    time.sleep(1)
    print("                    ")
    for i in board:
        st='|'
        for j in i:
            st= st+ str(j) +'|'  
        cprint(st,'blue')
        cprint("--------",'blue') 

    time.sleep(1)     
     



def make_empty_board():
    board= [ [1,2,3],[4,5,6],[7,8,9]]
    return board


def play(board,pos,p):
        #print(type(pos1))
        for row in board:
            #print(row)
            ind1=board.index(row)
            #print(ind1)
            if pos in row:
                #("true")
                ind2 = row.index(pos)
                #print(ind2)
                board[ind1][ind2]=p
                break
        #print(board)    
        DisplayBoard(board)


def check_winner(board,P):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    #X coordinates
    Win= None

    
    for row in range(0,3):
       if board[row][0]== P and board[row][1]== P and board[row][2]== P:
            Win=P
            print("conditon 1 satisfied")
            break   

      
    for col in range(0,3):
        if board[0][col]== P and board[1][col]== P and board[2][col]== P:
            Win=P
            print("conditon 2 satisfied")
            break      

    count=0    
    for i in range(0,3):
        if board[i][i]== P:
                count=count+1 
        if count==3:
            Win=P
            print("conditon 3 satisfied")
            break 

    count=0    
    for i in range(0,3):
        if board[i][2-i]== P:
                count=count+1 
        if count==3:
            Win=P
            print("conditon 4 satisfied")
            break     

    return Win 


def P1vsP2(board,P1, P2) :
    winner = None
    count=1
    pos1=0
    pos2=0
    li_pos=[1,2,3,4,5,6,7,8,9]
    no_pos=0
    #print(len(li_pos)==0)
    while winner == None and no_pos==0:
        try:
            pos1=int(input("player 1 enter Position:   "))
        except ValueError:
            print("Please input integer")   
            pos1=int(input("player 1 enter Position:   ")) 
        while pos1 not in li_pos:
            pos1=int(input("Position not available player 1 enter Position on board  "))

    

        i = li_pos.index(pos1)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break

        #print(li_pos)
        #########    
        play(board,pos1,P1)
        count=count+1

        win=check_winner(board,P1)
        if win == P1:
            print("Player1 '" +P1 +"' wins yayy")
            winner=P1
            break
        
        try:
            pos2=int(input("player 2 enter Position:   "))
        except ValueError:
            print("Please input integer")   
            pos2=int(input("player 2 enter Position:   "))     
        while pos2 not in li_pos:
            pos2=int(input("Position not available player 2 enter Position on board  "))

        i = li_pos.index(pos2)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break
        #print(li_pos)
        #########  
        play(board, pos2,P2)

        count=count+1
        win=check_winner(board,P2)
        if win == P2:
            print("Player2 '" +P2 +"' wins yayy")
            winner=P2
            break
        #print("this is count",count) 
        
    if winner == None:
        print("No winner draw")
        winner ="No winner draw"

        return winner





def P1vsBot(board,P1, P2) :
    winner = None
    count=1
    pos1=0
    pos2=0
    li_pos=[1,2,3,4,5,6,7,8,9]
    no_pos=0
    #print(len(li_pos)==0)
    #print("I am here")
    while winner == None and no_pos==0:
        try:
            pos1=int(input("player 1 enter Position:   "))
        except ValueError:
            print("Please input integer")   
            pos1=int(input("player 1 enter Position:   ")) 
        while pos1 not in li_pos:
            pos1=int(input("Position not available player 1 enter Position on board  "))

        i = li_pos.index(pos1)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break

        #print(li_pos)
        #########    
        play(board,pos1,P1)
        count=count+1

        win=check_winner(board,P1)
        if win == P1:
            print("Player1 '" +P1 +"' wins yayy")
            winner=P1
            break
        
        
        # using random.choice() to
        # get a random number
        pos2 = random.choice(li_pos)
        # printing random number
        print("Bot's choice of position is :    " + str(pos2))
        time.sleep(1) 

        i = li_pos.index(pos2)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break
        #print(li_pos)
        #########  
        play(board, pos2,P2)

        count=count+1
        win=check_winner(board,P2)
        if win == P2:
            print("Bot'" +P2 +"' wins yayy")
            winner=P2
            break
        #print("this is count",count) 
        
    if winner == None:
        print("No winner draw")
        winner ="No winner draw"

    
        return winner

#board=make_empty_board()
#win=P1vsBot(board,'X','O')




       



