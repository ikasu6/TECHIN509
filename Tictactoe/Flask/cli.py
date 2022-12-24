import numpy as np
import pickle
from flask import Flask,render_template, render_template_string, request, make_response
from easyAI import TwoPlayerGame
from termcolor import colored, cprint
from logic import Game,Bot,person,TicTacToe
import pandas as pd
import cgi
import matplotlib.pyplot as plt
import random
import time
app = Flask(__name__)
import io

#model = pickle.load(open("model.pkl", 'rb'))


@app.route('/')
def index():
    return render_template('index.html',data=[{'symbol': 'X'}, {'symbol': 'O'}])





@app.route("/play", methods=['GET', 'POST'])
def play():
    li=[0,0,0,0,0,0,0,0,0]
    if len(list(request.form.values()))== 3:

      print("NOTICEEEEEEEEEEEE______________________")
      print(list(request.form.values()))
      input_data = list(request.form.values())
      form = cgi.FieldStorage()
      g=form.getvalue('dropdown')
      print(g)
      print("__________________________")
      print(input_data)
      #mode=input_data[0]
      Mode=int(input_data[0])
      print("#############Mode###############")
      print(Mode)
      Player1_name=input_data[1]
      Player2_name=input_data[2]
      player1= person('X',1,Player1_name)
      prop1=player1.properties()
      player2= Bot('O',2,Player2_name)
      prop2=player2.properties()
      ttt=TicTacToe([player1,player2])
      msg=Player1_name+"  Vs  "+Player2_name
      msg2=''
      with open('Mode.pkl', 'wb') as file:  
        pickle.dump(Mode, file) 
      with open('player1.pkl', 'wb') as file:  
        pickle.dump(player1, file) 
      with open('player2.pkl', 'wb') as file: 
        pickle.dump(player2, file) 
      with open('ttt.pkl', 'wb') as file: 
        pickle.dump(ttt, file) 
      ttt.board=[0,0,0,0,0,0,0,0,0]
      c = ",".join(map(str, ttt.board))

    else:
      with open('Mode.pkl', 'rb') as file: 
        Mode = pickle.load(file)
      with open('player1.pkl', 'rb') as file: 
        player1 = pickle.load(file) 
      with open('player2.pkl', 'rb') as file: 
        player2 = pickle.load(file)
      with open('ttt.pkl', 'rb') as file:  
        ttt = pickle.load(file) 
      game_cookie = request.cookies.get("game_board")
      #gets the latest position on the board
      print(1)
      print(game_cookie)
      if game_cookie:
            ttt.board = [int(x) for x in game_cookie.split(",")]#converting it to list of list
      

      msg="Start here"
      msg2=''
      #Mode=1
      if Mode==1:
        
        msg="start here"
        winner=None
        

        if "choice" in request.form:
            
            msg = "Player1 Vs BOT "
            msg2=''
            print(request.form["choice"])
            t=ttt.play_move(request.form["choice"])
            print(t)
            if not ttt.is_over():
                print("getting move from bot.....")
                time.sleep(1)
                li2 = [i for i in range(len(ttt.board )) if ttt.board[i]==0 ]
                #ai_move = ttt.get_move()
                ai_move=random.choice(li2)
                print(ai_move)
                ttt.play_move(ai_move)
            
        if "reset" in request.form:
            ttt.board = [0 for i in range(9)]
        if ttt.is_over():
            print("Somebody woen")
            msg = ttt.winner()
            msg2="Click Here for Results"
            if msg=="Player1 Wins":
              player1.GS='Win'
              player2.GS='NoWin'
            elif msg=="Player2 Wins":
              player1.GS='NoWin'
              player2.GS='Win'
            else:
              player1.GS='Draw'
              player2.GS='Draw'
            finaldict={'PlayerName':[player1.Title,player2.Title],'PlayerStatus':[player1.GS,player2.GS],'PlayerType':['Person','Bot']}
            games_data=pd.read_csv('out2.csv',index_col=[0])
            GID=list(games_data["GameID"])
            finaldict["GameID"]=[GID[-1]+1,GID[-1]+1]
            print(finaldict)
            #columns1=["PlayerName","PlayerStatus","PlayerType" ,"GameID"]
            for k in range(2):
                li=[]
                for i in finaldict:

                    am= finaldict[i][k]
                    li.append(am)
                games_data.loc[len(games_data.index)] = li
            games_data.to_csv('out2.csv')
        
        if "reset" in request.form:
            ttt.board = [0 for i in range(9)]
        print("I'm here 1")
        
        c = ",".join(map(str, ttt.board))


        n=ttt.board.count(2)
        p=ttt.board.count(1)




        

      
      ###############################3
      if Mode==2:
        
        msg="Player1(X) Vs Player2(O)"
        msg2=''
        winner=None
        game_cookie = request.cookies.get("game_board")
        #gets the latest position on the board
        print(1)
        print(game_cookie)
        if game_cookie:
              ttt.board = [int(x) for x in game_cookie.split(",")]#converting it to list of list
        
        print(2)    
        print(ttt.board)
        ct=ttt.board.count(0)
        if ct%2==1:
          
          ttt.assign(2)
        else:
        
          ttt.assign(1)
        
        if "choice" in request.form:#If player 1 clicked any choice
              pos1=ttt.play_move(request.form["choice"])
              print(3)
              print(pos1)

        if "reset" in request.form:
            ttt.board = [0 for i in range(9)]
        if ttt.is_over():
            msg = ttt.winner()
            msg2="Click Here for Results"
            if msg=="Player1 Wins":
              player1.GS='Win'
              player2.GS='NoWin'
            elif msg=="Player2 Wins":
              player1.GS='NoWin'
              player2.GS='Win'
            else:
              player1.GS='Draw'
              player2.GS='Draw'
            
            finaldict={'PlayerName':[player1.Title,player2.Title],'PlayerStatus':[player1.GS,player2.GS],'PlayerType':['Person','Person']}
            games_data=pd.read_csv('out2.csv',index_col=[0])
            GID=list(games_data["GameID"])
            finaldict["GameID"]=[GID[-1]+1,GID[-1]+1]
            columns1=["PlayerName","PlayerStatus","PlayerType" ,"GameID"]
            for k in range(2):
                li=[]
                for i in finaldict:
                    ap= finaldict[i][k]
                    li.append(ap)
                    print(li)
                games_data.loc[len(games_data.index)] = li
            games_data.to_csv('out2.csv')
            
        
        if "reset" in request.form:
            ttt.board = [0 for i in range(9)]
        print("I'm here 1")

        c = ",".join(map(str, ttt.board))


        n=ttt.board.count(2)
        p=ttt.board.count(1)

    #c = ",".join(map(str, ttt.board))   

    resp = make_response(render_template("Play.html", ttt=ttt, msg=msg,msg2=msg2))
    print(resp)
    print(c)
    resp.set_cookie("game_board", c)

    print("I'm here 2")

    return resp



@app.route('/result', methods=("POST", "GET"))
def results():
  with open('player1.pkl', 'rb') as file: 
        player1 = pickle.load(file) 
  with open('player2.pkl', 'rb') as file: 
        player2 = pickle.load(file)
  with open('Mode.pkl', 'rb') as file: 
        Mode = pickle.load(file)

  games_data=pd.read_csv('out2.csv',index_col=False)
  li2=games_data.PlayerName[games_data['PlayerStatus']=='Win'] 
  li2=list(li2)
  df2=games_data.explode('PlayerName')
  res = pd.crosstab(df2['PlayerName'], df2['PlayerStatus'])
   
  res['GamesPlayed']=res['Draw'] + res['NoWin'] + res['Win'] 
        
            
  res=res[['GamesPlayed', 'Draw', 'NoWin', 'Win']]
  res.columns.name = None      
  res=res.sort_values('Win',ascending=False)
  res.reset_index(inplace=True)
  rankboard=res.head(5)#.to_string
  rankboard=rankboard.reset_index(drop=True)
  P1data=res.loc[res['PlayerName'] == player1.Title]
  P2data=res.loc[res['PlayerName'] == player2.Title]
  #P1data=P1data.to_string(index=False)
  '''print( P1data)
  print(P1data['PlayerName'])
  print(P2data['PlayerName'])
  print(P1data['GamesPlayed'][0])
  print(P1data['Win'][0])
  print(P2data['PlayerName'][0], P2data['GamesPlayed'][0],P2data['Win'][0])'''
  if Mode==1:
    #P1="Player1Name : " +str(P1data['PlayerName'][1])+ "  ||  GamesPlayed : " +str(P1data['GamesPlayed'][1])+ "  ||  Won : " +str(P1data['Win'][1])
    P1="Player1Name : " +str(P1data['PlayerName'])+ "  ||  GamesPlayed : " +str(P1data['GamesPlayed'])+ "  ||  Won : " +str(P1data['Win'])
    P2="Player2Name : " +str(P2data['PlayerName'])+ "  ||  GamesPlayed : " +str(P2data['GamesPlayed'])+ "||  Won : " +str(P2data['Win'])
    
  else:
    P1="Player1Name : " +str(P1data['PlayerName'][1])+ "  ||  GamesPlayed : " +str(P1data['GamesPlayed'][1])+ "  ||  Won : " +str(P1data['Win'][1])
    P2="Player2Name : " +str(P2data['PlayerName'][0])+ "  ||  GamesPlayed : " +str(P2data['GamesPlayed'][0])+ "||  Won : " +str(P2data['Win'][0])

  


  '''print(P1)
  P2data=res.loc[res['PlayerName'] == player2.Title]
  print(P2data)
  print(str(P2data['PlayerName'][0]))
  print(str(P2data['GamesPlayed'][1]))
  print(str(P2data['Win'][1]))'''
  '''try:
    P2="Player2Name : " +str(P2data['PlayerName'][0])+ "  ||  GamesPlayed : " +str(P2data['GamesPlayed'][0])+ "||  Won : " +str(P2data['Win'][0])
  except KeyError: 
    P2="Player2Name : " +str(P2data['PlayerName'][1])+ "  ||  GamesPlayed : " +str(P2data['GamesPlayed'][1])+ "||  Won : " +str(P2data['Win'][1])
  print(P2)'''

  rankboard.plot.barh(x='PlayerName', y='Win',
	title='Top 5 Players', color='Blue')
  plt.savefig('templates/graph.png')
  #P2data=P2data.to_string(index=False)
  
  #return render_template('stats.html',tables=[P1data.to_html(classes='player1'), P2data.to_html(classes='player2'),rankboard.to_html(classes='page')])
  rankboard.reset_index(drop=True,inplace=True)
  print(rankboard)
  data={"PlayerName":"Win"}
  pn=rankboard['PlayerName']
  win=rankboard['Win']
  for i in range(5):
    k=pn[i]
    data[k]=win[i]
  print(data)


  
  
  return render_template('stats.html', data=data ,msg1=P1,msg2=P2,tables=[rankboard.to_html(classes='page')])


          
          
        





    

if __name__ == "__main__":
    app.run(debug=True)

#results()
       
   