from flask import Flask, jsonify, request
from flask_cors import CORS
from sklearn import svm

app = Flask(__name__)
CORS(app)

history = [1,2,3,2,1,3,1,3,1,1,2,3,1,3,2,3,2,2,2,3,3,1,1,3,1,2,1,2,3,1,3,2,1,3,2,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]

#Player 1 Model
input_data = [
  [1,2,3,2],
  [2,3,2,1],
  [3,2,1,3],
  [2,1,3,1],
  [1,3,1,3],
  [3,1,3,1],
  [1,3,1,1],
  [3,1,1,2],
  [1,1,2,3],
  [1,2,3,1],
  [2,3,1,3],
  [3,1,3,2],
  [1,3,2,3],
  [3,2,3,2],
  [2,3,2,2],
  [3,2,2,2],
  [2,2,2,3],
  [2,2,2,3],
  [2,3,3,1],
  [3,3,1,1],
  [3,1,1,3],
  [1,1,3,1],
  [1,3,1,2],
  [3,1,2,1],
  [1,2,1,2],
  [2,1,2,3],
  [1,2,3,1],
  [2,3,1,3],
  [3,1,3,2],
  [1,3,2,1],
  [3,2,1,3],
  [2,1,3,2],
  [1,3,2,1],
  [3,2,1,2],
  [2,1,2,3],
  [1,2,3,1],
  [2,3,1,2],
  [3,1,2,3],
  [1,2,3,1],
  [2,3,1,2],
  [3,1,2,3],
  [1,2,3,1],
  [2,3,1,2],
  [3,1,2,3],
  [1,2,3,1],
  [2,3,1,2],
  [3,1,2,3],
  [1,2,3,1]
]

output_data = [1,3,1,3,1,1,2,3,1,3,2,3,2,2,2,3,3,1,1,3,1,2,1,2,3,1,3,2,1,3,2,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2]

model = svm.SVC()
model.fit(input_data, output_data)

def getPlayer1():
  data_record = [history[-4],history[-3],history[-2], history[-1]]
  current = model.predict([data_record])[0]
  if current == 1:
    return 2
  if current == 2:
    return 3
  return 1

win = 0
lose = 0
tied = 0

@app.route("/Game",methods=["POST"])
def getgame():
  global win, lose, tied
  resultslist = []
  results = ""
  comp = getPlayer1()
  user = request.json.get("move")

  comp_str = ''
  if comp == 1:
    comp_str = "rock"
  elif comp == 2:
    comp_str = "paper"
  elif comp == 3:
    comp_str = "scissors"

  user_str = ''
  if user == 1:
    user_str = "rock"
  elif user == 2:
    user_str = "paper"
  elif user == 3:
    user_str = "scissors"

  
  if comp == 1 and user == 1:
    results = "It's a tie"
    tied += 1
  elif comp == 1 and user  == 2:
    results = "You win!"
    win += 1
  elif comp == 1 and user == 3:
    results = "You lose"
    lose += 1

  #Paper
  elif comp == 2 and user == 2:
    results = "It's a tie"
    tied += 1
  elif comp == 2 and user  ==3:
    results = "You win!!"
    win+=1
  elif comp == 2 and user == 1:
    results = "You lost"
    lose += 1
  #Scissors
  elif comp == 3 and user == 3:
    results = "It's a tie"
    tied += 1
  elif comp == 3 and user  == 1:
    results = "You win!!"
    win += 1
  elif comp == 3 and user == 2:
    results = "You lost"
    lose += 1


  history.append(user)
  input_data.append([history[-5], history[-4], history[-3], history[-2]])
  output_data.append(history[-1])
  model.fit(input_data,output_data)
  

  resultslist.append({
    "comp": comp_str,
    "user": user_str,
    "result": results,
    "win": win,
    "lose": lose,
    "tied": tied
  })
  
  return jsonify(resultslist[0])

if __name__ == '__main__':
  app.run(host = '0.0.0.0')

