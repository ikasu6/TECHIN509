# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

from termcolor import colored, cprint
import time
import random

def DisplayBoard(board: list)-> None: 
    
    cprint("*TICTACTOE BOARD*",'magenta')
    time.sleep(1)
    print("                    ")
    for x in board:
        st='|'
        for y in x:
            st= st+ str(y) +'|'  
        cprint(st,'blue')
        cprint("--------",'blue') 

    time.sleep(1)     
     



def make_empty_board():#can Unit test
    board= [ [1,2,3],[4,5,6],[7,8,9]]
    return board


def play(board: list,pos: int,p: str)->None:
        
        for row in board:
            
            ind1=board.index(row)
            
            if pos in row:
               
                ind2 = row.index(pos)

                board[ind1][ind2]=p
                break
    
        DisplayBoard(board)


def check_winner(board: int,P: str)-> str :
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


def P1vsP2(board: list,P1: str, P2: str)->str :
    winner = None
    count=1
    pos1=0
    pos2=0
    li_pos=[1,2,3,4,5,6,7,8,9]
    no_pos=0
    
    while winner == None and no_pos==0:
        try:
            pos1=int(input("player 1 enter Position:   "))
        except ValueError:
            print("Please input integer")   
            pos1=int(input("player 1 enter Position:   ")) 

        while pos1 not in li_pos:
            pos1=int(input("Position not available player 1 enter Position on board  "))

    
        play(board,pos1,P1)
        count=count+1
        i = li_pos.index(pos1)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break

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

        
         
        play(board, pos2,P2)
        i = li_pos.index(pos2)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break

        count=count+1
        win=check_winner(board,P2)
        if win == P2:
            print("Player2 '" +P2 +"' wins yayy")
            winner=P2
            break
        
        
    if winner == None:
        print("No winner draw")
        winner ="No winner draw"

        return winner





def P1vsBot(board: list,P1: str, P2: str)-> str:
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

        
        play(board,pos1,P1)
        count=count+1
        i = li_pos.index(pos1)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break

        win=check_winner(board,P1)
        if win == P1:
            print("Player1 '" +P1 +"' wins yayy")
            winner=P1
            break
        

        pos2 = random.choice(li_pos)
        # printing random number
        print("Bot's choice of position is :    " + str(pos2))
        time.sleep(1) 


  
        play(board, pos2,P2)
        i = li_pos.index(pos2)
        del li_pos[i]
        if len(li_pos)==0:
            no_pos=1
            break

        count=count+1
        win=check_winner(board,P2)
        if win == P2:
            print("Bot'" +P2 +"' wins yayy")
            winner=P2
            break
 
        
    if winner == None:
        print("No winner draw")
        winner ="No winner draw"

    
        return winner



class player1:
    
    def __init__(self, P1: str, Mode: int)-> None:
        self.Mode=Mode
        self.P1 = P1
        self.assign()
            
        
    def assign(self):
        self.Title='Player1'
        #print(self.Mode,self.P1,self.Title)
        return (self.P1,self.Mode,self.Title)



class player2:
    
    def __init__(self, P1: str, Mode: int)-> None:
        self.Mode=Mode
        self.P1 = P1
        self.assign()
            
        
    def assign(self):



        if self.Mode==1:
            cprint("Single Player Game",'red')
            cprint("Player1 Vs Bot",'cyan')

            self.Title= "Bot"
            if self.P1=='X':
                    self.P2 ='O'
                    print("Player1:  ",self.P1 )
                    print("Bot:      ",self.P2 )
            elif self.P1=='O' :
                    self.P2='X'
                    print("Player1:  ",self.P1 ) 
                    print("Bot:      ",self.P2 )
                    print(self.Mode,self.P2,self.Title)
                
        if self.Mode==2:
            cprint("Double Player Game",'red')
            cprint("Player1 Vs Player2",'cyan')
            self.Title= "Player2"
            if self.P1=='X':
                self.P2='O'
                print("Player1:  ",self.P1 )
                print("Player2:  ",self.P2 )
            elif self.P1=='O' :
                self.P2='X'
                print("Player1:  ",self.P1 ) 
                print("Player2:  ",self.P2 )
                
        return (self.P2,self.Mode,self.Title) 



       



