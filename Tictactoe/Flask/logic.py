# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

from termcolor import colored, cprint
import time
import random


class Bot:
    def __init__(self, Sym: str, Pn: int)-> None:
        self.Sym = Sym #['x'] or 'o']
        self.Pn=Pn
        self.assign()

    def assign(self):   
        self.Title= input("Enter a name for bot player"+str(self.Pn)+" :  ")
        cprint(self.Title+" : '"+self.Sym+"'",'green')
        self.GS=None
        self.positions=[]
        return (self.Sym,self.Title) 

    def get_position(self,li_pos:list)->int: 
        self.li_pos=li_pos
        self.pos = random.choice(li_pos)
        # printing random number
        print(self.Title+"'s choice of position is :    " + str(self.pos))
        self.i = self.li_pos.index(self.pos)
        del self.li_pos[self.i]
        time.sleep(1)
        return (self.pos ,self.li_pos) 

    def properties(self):
        self.prop={'Name':self.Title,'Moves':self.positions,'Status':self.GS,'Symbol':self.Sym,'Type':'Bot'}  
        return(self.prop) 





class person:
    def __init__(self, Sym: str,Pn: int)-> None:
        #self.Mode= Mode
        self.Sym = Sym #['x'] or 'o']
        self.Pn=Pn
        self.assign()

    def assign(self):
        self.Title=input(" Please Enter your name "+"Player"+str(self.Pn)+":  ")
        cprint(self.Title+" : '"+self.Sym+"'",'green')
        self.GS=None
        self.positions=[]
        return (self.Sym,self.Title) 
   

    def get_position(self,li_pos:list)->int: 

        ##########
        self.li_pos=li_pos
        #print(self.li_pos)
        
        try:
            self.pos=int(input(self.Title +" enter Position:   "))
            print(self.pos)
        except ValueError:
            print("Please input integer")   
            self.pos=int(input(self.Title +" enter Position:   "))
        while self.pos not in self.li_pos:
            self.pos=int(input("Position not available! "+self.Title+" enter Position:   "))

        self.i = self.li_pos.index(self.pos)
        del self.li_pos[self.i]
        #DisplayBoard(self.li_pos)    

        return (self.pos ,self.li_pos) 

    def properties(self):
        self.prop={'Name':self.Title,'Moves':self.positions,'Status':self.GS,'Symbol':self.Sym, 'Type':'Bot'} 
        return(self.prop)    



########################################################

    
     

def make_empty_board():#can Unit test
    board= [ [1,2,3],[4,5,6],[7,8,9]]
    return board

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


def get_positions_onboard(board: list,pos: int,p: str)->None:
    
    for row in board:
            
            ind1=board.index(row)
            
            if pos in row:
               
                ind2 = row.index(pos)

                board[ind1][ind2]=p
                break
    
    DisplayBoard(board)
    return board


def check_winner(board: int,P: str)-> str :
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    #X coordinates
    #print(board)
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















