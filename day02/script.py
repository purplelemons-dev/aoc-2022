
with open("input", 'r') as f: data = [x.strip() for x in f.readlines()]

shapeScore = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

roundScore = {
    "lost": 0,
    "tie": 3,
    "win": 6
}

translate = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

score=0

def getScore(player1, player2):
    gameScore = 0
    if player1 == player2: gameScore+=roundScore["tie"]
    elif player1 == "rock" and player2 == "scissors": gameScore+=roundScore["win"]
    elif player1 == "paper" and player2 == "rock": gameScore+=roundScore["win"]
    elif player1 == "scissors" and player2 == "paper": gameScore+=roundScore["win"]
    else: gameScore+=roundScore["lost"]
    return gameScore+shapeScore[player1]

for i in data:
    player1, player2 = i.split(" ")
    player1, player2 = translate[player1], translate[player2]
    score+=getScore(player2, player1)

print(f"### Part 1 ###\n{score= }")
