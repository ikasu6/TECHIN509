# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import time
from termcolor import colored, cprint
from logic import make_empty_board, DisplayBoard, check_winner,play,P1vsP2,P1vsBot
from logic import player1, player2



    
    


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
        try:
            Mode= int(input("Enter: "))
        except:
            cprint("Enter Valid details",'red')    
        


    while P1 != 'O' and P1 !='X':
        try:
            P1=input("Player1 select your symbol X or O: ")
            P1=P1.upper()
        except:
            cprint("Enter Valid details",'red')     
            


    Player1=player1(P1,Mode)
    Player2=player2(Player1.P1,Player1.Mode)# dependency Injection
    P2=Player2.P2
    
    
if Mode==1:
    winner=P1vsBot(board,P1, P2)
    #print(winner)
    pass
if Mode==2:
    winner=P1vsP2(board,P1, P2)
    #print(winner)