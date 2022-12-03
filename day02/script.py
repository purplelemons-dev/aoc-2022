
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

### Part 2 ###

score=0

translate = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

winLose = {
    "X": "lose",
    "Y": "tie",
    "Z": "win"
}

def getScore(elfChoice, outcome):
    gameScore = 0
    if outcome=="win":
        gameScore+=roundScore["win"]
        if elfChoice=="rock": gameScore+=shapeScore["paper"]
        elif elfChoice=="paper": gameScore+=shapeScore["scissors"]
        elif elfChoice=="scissors": gameScore+=shapeScore["rock"]
    elif outcome=="tie":
        gameScore+=roundScore["tie"]
        gameScore+=shapeScore[elfChoice]
    else:
        gameScore+=roundScore["lost"]
        if elfChoice=="rock": gameScore+=shapeScore["scissors"]
        elif elfChoice=="paper": gameScore+=shapeScore["rock"]
        elif elfChoice=="scissors": gameScore+=shapeScore["paper"]
    return gameScore

for i in data:
    elfChoice, outcome = i.split(" ")
    elfChoice = translate[elfChoice]
    outcome = winLose[outcome]

    score+=getScore(elfChoice, outcome)

print(f"### Part 2 ###\n{score= }") # >13386
