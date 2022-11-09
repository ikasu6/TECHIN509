# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

def DisplayBoard(board):
    
    print("*TICTACTOE BOARD*")
    print("                    ")
    for i in board:
        st='|'
        for j in i:
            st= st+ str(j) +'|'  
        print(st)
        print("--------")  
     



def make_empty_board():
    board= [ [1,2,3],[4,5,6],[7,8,9]]
    return board


def play(board,pos,p):
        #print(type(pos1))
        for row in board:
            print(row)
            ind1=board.index(row)
            print(ind1)
            if pos in row:
                ("true")
                ind2 = row.index(pos)
                print(ind2)
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



