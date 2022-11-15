# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import time
from termcolor import colored, cprint
from logic import make_empty_board, DisplayBoard, check_winner,play,P1vsP2,P1vsBot


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
        #print(self.Mode)

        #print("Check")


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
            
    
    
    
    

        




if __name__ == '__main__':
    
    GameName= "**********TicTacToe Game***********"
    cprint(GameName, "green")
    time.sleep(1)
    board = make_empty_board()
    print("               ")
    DisplayBoard(board)
    print("               ")

    #getting input
    Mode=0
    P1='N'
    while Mode!=1 and Mode!=2:
        cprint("Press 1 for Single player mode","yellow")
        cprint("Press 2 for Double player mode","yellow")
        Mode= int(input("Enter: "))

    while P1 != 'O' and P1 !='X':
        P1=input("Player1 select your symbol X or O: ")
        P1=P1.upper()


    Player1=player1(P1,Mode)
    Player2=player2(Player1.P1,Player1.Mode)
    #print("this Player2 P2",Player2.P2)
    P2=Player2.P2
    #############################
    
if Mode==1:
    winner=P1vsBot(board,P1, P2)
    print(winner)
    pass
if Mode==2:
    winner=P1vsP2(board,P1, P2)
    print(winner)