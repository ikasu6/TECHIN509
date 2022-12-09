# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import time
from termcolor import colored, cprint
from logic import make_empty_board, DisplayBoard,Bot,person, get_positions_onboard, check_winner
import pandas as pd


    
    


if __name__ == '__main__':
    
    GameName= "**********TicTacToe Game***********"
    cprint(GameName, "green")
    time.sleep(1)
    #printing top player

    def winnerboard(filename):
        games_data=pd.read_csv(filename,index_col=[0])
        li2=games_data.PlayerName[games_data['PlayerStatus']=='Win'] 
        li2=list(li2)
        Player_won_max=max(li2,key=li2.count)
        No_of_times_won=li2.count(Player_won_max)
        No_of_games_Played=len(games_data[games_data['PlayerName']==Player_won_max] )
        df2=games_data.explode('PlayerName')
        #print(df2)
        res = pd.crosstab(df2['PlayerName'], df2['PlayerStatus'])
        #print(res)
        res['GamesPlayed']=res['Draw'] + res['NoWin'] + res['Win'] 
        
            
        res=res[['GamesPlayed', 'Draw', 'NoWin', 'Win']]
        res.columns.name = None
        return res

    res=winnerboard('out.csv') 
    res=res.sort_values('Win',ascending=False)
    res.reset_index(inplace=True)
    #res['Rank']=[x+1 for x in list(res.index)]
    rankboard=res.head(4).to_string(index=False)

    cprint("_____________________________________________________________________________","red")
    cprint("            *******************Our Top Players*********************          ", "red")
    cprint(rankboard,"red")
    cprint("-----------------------------------------------------------------------------","red")



    board = make_empty_board()
    print("               ")
    DisplayBoard(board)
    print("               ")
    ###storing Variables#############

    ###############################3

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
            #print("Printing length of li",li)
            if len(li)!=0:
                (pos1,ln)=player1.get_position(li)
                li=ln
                player1.positions.append(pos1)
                board_updated=get_positions_onboard(board,pos1,P1)
                winner=check_winner(board_updated,P1)
                if winner==player1.Sym:
                    cprint(player1.Title +"  '"+player1.Sym+ "' won the game",'magenta') 
                    player1.GS='Win'
                    player2.GS='NoWin'
                    break
 
              
            #print("Printing length of li",li)
            if len(li)!=0:
                (pos2,ln)=player2.get_position(li)
                li=ln
                player2.positions.append(pos2)
                board_updated=get_positions_onboard(board,pos2,P2)
                winner=check_winner(board_updated,P2)

                if winner == player2.Sym:
                        cprint(player2.Title +"  '"+player2.Sym+ "' won the game",'magenta')
                        player1.GS='NoWin'
                        player2.GS='Win'
                           
                        break


       
            if len(li)==0 and winner==None:
                cprint("DRAW no one won the game",'magenta')
                
                player1.GS='Draw'
                player2.GS='Draw'
                break


    #print(player1.properties())  
    #print(player2.properties()) 
    l=[]
    finaldict={}
    for i in player1.properties():
     newkey='Player'+i
     finaldict[newkey]=[player1.properties()[i],player2.properties()[i]]

    



    

    try:
        games_data=pd.read_csv('out.csv',index_col=[0])
        #print(games_data.columns)
        #print(len(games_data.columns))
        GID=list(games_data["GameID"])
        finaldict["GameID"]=[GID[-1]+1,GID[-1]+1]
        columns1=["PlayerName","PlayerMoves","PlayerStatus","PlayerSymbol","PlayerType" ,"GameID"]
        for k in range(2):
            li=[]
            for i in finaldict:
                a= finaldict[i][k]
                li.append(a)
                #print("fgshjehjrkjrkdjf,,h")
                
            #print(li)
            games_data.loc[len(games_data.index)] = li
        games_data.to_csv('out.csv')



        
    except FileNotFoundError:
        
        columns1=["PlayerName","PlayerMoves","PlayerStatus","PlayerSymbol","PlayerType" ,"GameID"]
        finaldict["GameID"]=[1,1]
        li=[]
        for i in finaldict:
           a= finaldict[i]
           li.append(a)
        data_df = pd.DataFrame(li)
        data_df = data_df.transpose()
        data_df.columns = columns1
        #print(data_df.head())
        #data_df.set_index('GameID')
        #print(data_df)
        data_df.to_csv('out.csv')

    res=winnerboard('out.csv') 
    res=res.sort_values('Win',ascending=False)
    res.reset_index(inplace=True)
    #res['Rank']=[x+1 for x in list(res.index)]
    rankboard=res.head(4).to_string(index=False)
    P1data=res.loc[res['PlayerName'] == player1.Title]
    P1data=P1data.to_string(index=False)
    cprint("Great Game !!!",'yellow')
    cprint("_______________________________", 'green')
    cprint(player1.Title+" your details",'green')
    cprint(P1data,'green')
    P2data=res.loc[res['PlayerName'] == player2.Title]
    P2data=P2data.to_string(index=False)
    cprint("_______________________________", 'green')
    cprint(player2.Title+"  your details",'green')
    cprint(P2data,'green')

    




        

  






