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

    

class Game():
    def __init__(self, Player1:object, Player2:object)-> None:
        #self.Mode= Mode
        self.Player1 = Player1
        self.Player2 = Player2
        self.Board= [ [1,2,3],[4,5,6],[7,8,9]]
        #self.assign()

    def make_empty_board():#can Unit test
        board= [ [1,2,3],[4,5,6],[7,8,9]]
        return board    



    def DisplayBoard(self, board: list)-> None: 
        
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


    def get_positions_onboard(self,board: list,pos: int,p: str)->None:
        
        for row in board:
                
                ind1=board.index(row)
                
                if pos in row:
                
                    ind2 = row.index(pos)

                    board[ind1][ind2]=p
                    break
        
        #DisplayBoard(board)
        return board


    def check_winner(self,board: int,P: str)-> str :
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


    '''def play(self,Player1:object,  Player2:object):
        li=[1,2,3,4,5,6,7,8,9]
        winner=None
        while winner==None:
            #print("Printing length of li",li)
            if len(li)!=0:
                (pos1,ln)=Player1.get_position(li)
                li=ln
                Player1.positions.append(pos1)
                board_updated= Game.get_positions_onboard(Board,pos1,P1)
                winner=Game.check_winner(board_updated,P1)
                if winner==Player1.Sym:
                    cprint(Player1.Title +"  '"+Player1.Sym+ "' won the game",'magenta') 
                    Player1.GS='Win'
                    Player2.GS='NoWin'
                    break
 
              
            #print("Printing length of li",li)
            if len(li)!=0:
                (pos2,ln)=Player2.get_position(li)
                li=ln
                Player2.positions.append(pos2)
                board_updated=Game.get_positions_onboard(Board,pos2,P2)
                winner=Game.check_winner(board_updated,P2)

                if winner == Player2.Sym:
                        cprint(Player2.Title +"  '"+Player2.Sym+ "' won the game",'magenta')
                        Player1.GS='NoWin'
                        Player2.GS='Win'
                           
                        break


       
            if len(li)==0 and winner==None:
                cprint("DRAW no one won the game",'magenta')
                
                Player1.GS='Draw'
                Player2.GS='Draw'
                break



        l=[]
        finaldict={}
        for i in Player1.properties():
            newkey='Player'+i
            finaldict[newkey]=[Player1.properties()[i],Player2.properties()[i]]'''
     















