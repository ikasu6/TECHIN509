# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

from termcolor import colored, cprint
import time
import random
from easyAI import TwoPlayerGame

class Bot:
    def __init__(self, Sym: str, Pn: int, Title: str)-> None:
        self.Sym = Sym #['x'] or 'o']
        self.Pn=Pn
        self.Title=Title
        self.assign()

    def assign(self):   
        
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
    def __init__(self, Sym: str,Pn: int,Title:str)-> None:
        #self.Mode= Mode
        self.Sym = Sym #['x'] or 'o']
        self.Pn=Pn
        self.Title=Title
        self.assign()

    def assign(self):
        
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
        self.board= [[1,2,3],[4,5,6][7,8,9]]
        #self.assign()


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

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[3 * j + i]]

    def show(self):
        print(
            "\n"
            + "\n".join(
                [
                    " ".join([[".", "O", "X"][self.board[3 * j + i]] for i in range(3)])
                    for j in range(3)
                ]
            )
        )


class TicTacToe(TwoPlayerGame):
    """The board positions are numbered as follows:
    1 2 3
    4 5 6
    7 8 9
    """

    def __init__(self, players):
        self.players = players
        self.board = [0,0,0,0,0,0,0,0,0]
        self.current_player = 1  # player 1 starts.
        
    def assign(self,n):
        self.current_player=n

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.current_player

    def make_move1(self, move):
        self.board[int(move) - 1] = self.current_player2

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],  # horiz.
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],  # vertical
        [1, 5, 9],
        [3, 5, 7],  # diagonal
    ]

    def lose(self, who=None):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.opponent_index
        wins = [
            all([(self.board[c - 1] == who) for c in line]) for line in self.WIN_LINES
        ]
        return any(wins)

    def is_over(self):
        #print(self.current_player)
        return (
            (self.possible_moves() == [])
            or self.lose()
            or self.lose(who=self.current_player)
            #or self.lose(who=self.current_player2)
        )

    def show(self):
        print(
            "\n"
            + "\n".join(
                [
                    " ".join([[".", "O", "X"][self.board[3 * j + i]] for i in range(3)])
                    for j in range(3)
                ]
            )
        )

    def spot_string(self, i, j):
        #print("This is J and I",(j,i))
        return ["_", "O", "X"][self.board[3 * j + i]]

    def scoring(self):
        opp_won = self.lose()
        i_won = self.lose(who=self.current_player)
        if opp_won and not i_won:
            return -100
        if i_won and not opp_won:
            return 100
        return 0

    def winner(self):
        if self.lose(who=1):
            return "Player2 Wins"
        if self.lose(who=2):
            return "Player1 Wins" 
        return "Tie"

     















