# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import time
from termcolor import colored, cprint
from logic import make_empty_board, DisplayBoard,Bot,person,play, get_positions_onboard, check_winner




    
    


if __name__ == '__main__':
    
    GameName= "**********TicTacToe Game***********"
    cprint(GameName, "green")
    time.sleep(1)
    board = make_empty_board()
    print("               ")
    DisplayBoard(board)
    print("               ")

    #Initiation
    Mode= None
    P1='N'
    winner=None
    li=[1,2,3,4,5,6,7,8,9]
    sym=['X','O']
    mode_list=[1,2,3]
    while Mode not in mode_list:
        cprint("Press 1 for Single player mode","yellow")
        cprint("Press 2 for Double player mode","yellow")
        cprint("Press 3 for Bot Double player mode","yellow")
        try:
            Mode= int(input("Enter: "))
        except:
            cprint("Enter Valid details",'red')    
        


    while P1 != 'O' and P1 !='X':
        try:
            P1=input("Select symbol for Player 1 'X' or 'O' : ")
            P1=P1.upper()
            if P1==sym[0]:#X
                P2='O'
            else:
                P2='X'    

        except:
            cprint("Enter Valid details",'red')     
            
    ##Defining Mode
    
    if Mode==1:
        #This is single player mode 
        player1= person(P1,1)
        player2= Bot(P2,2)

    if Mode==2:
        #This is  Double player mode
        player1= person(P1,1)
        player2= person(P2,2)    

    if Mode==3:
        #This is  Bot Double player mode
        player1= Bot(P1,1)
        player2= Bot(P2,2)
        
    while winner==None:
            print("Printing length of li",li)
            if len(li)!=0:
                (pos1,ln)=player1.get_position(li)
                li=ln
                board_updated=get_positions_onboard(board,pos1,P1)
                winner=check_winner(board_updated,P1)
                if winner==player1.Sym:
                    cprint(player1.Title +"  '"+player1.Sym+ "' won the game",'magenta') 
                    break
 
              
            print("Printing length of li",li)
            if len(li)!=0:
                (pos2,ln)=player2.get_position(li)
                li=ln
                board_updated=get_positions_onboard(board,pos2,P2)
                winner=check_winner(board_updated,P2)

                if winner == player2.Sym:
                        cprint(player2.Title +"  '"+player2.Sym+ "' won the game",'magenta')  
                        break


       
            if len(li)==0 and winner==None:
                cprint("DRAW no one won the game",'magenta')
                  


    
    
    