# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import DisplayBoard
from logic import check_winner
from logic import play





if __name__ == '__main__':
   
 
    board = make_empty_board()
    print("               ")
    DisplayBoard(board)
    print("               ")


    #getting input
    P1=input("Player1 select your symbol X or O: ")
    
    if  P1== 'X' or P1== 'O':
        #print("Player1:  ",P1)
        pass
    else:
        P1=input("Please Enter X or O:  ")    
    
    while P1 !='X' and P1 !='O':
        P1=input("Please Enter X or O:  ")  

    if P1=='X':
        P2='O'
        print("Player1:  ",P1 )
        print("Player2:  ",P2 )
    elif P1=='O' :
        P2='X'
        print("Player1:  ",P1 ) 
        print("Player2:  ",P2 )   
    


    
 
    winner = None
    count=1
    while winner == None and count<=9:
        try:
            pos1=int(input("player 1 enter Position:   "))
        except ValueError:
            print("Please input integer")   
            pos1=int(input("player 1 enter Position:   ")) 
        while pos1 not in board[0] and pos1 not in board[1] and pos1 not in board[2]:
            pos1=int(input("Position not available player 1 enter Position on board  "))
        play(board,pos1,P1)
        count=count+1
        #print("this is count",count)
        #play(pos1,P1)
        #count=count+1
        #print("this is count",count)
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
        while pos2 not in board[0] and pos2 not in board[1] and pos2 not in board[2]:
            pos2=int(input("Position not available player 2 enter Position on board  "))
        
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

        # TODO: Show the board to the user. done
        # TODO: Input a move from the player.
        # TODO: Update the board.
        # TODO: Update who's turn it is.
        #winner = 'X'  # FIXME