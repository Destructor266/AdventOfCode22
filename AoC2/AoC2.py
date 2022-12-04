"""
The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. 
The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). 
This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). 
This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to your strategy guide?
"""
points = 0

for move in open("E:/Programacion/Python/AdventOfCode/AoC2/RockPaperScissors.txt", "r"):
    OpponentMove = move[0:1]
    #print(OpponentMove)
    OwnMove = move[1:-1]
    OwnMove = OwnMove.lstrip()
    #print(OwnMove)

    if (OwnMove == "X"):
        points += 1
    elif (OwnMove == "Y"):
        points += 2
    elif (OwnMove == "Z"):
        points += 3

    if (OpponentMove == "A" and OwnMove == "X" or OpponentMove == "B" and OwnMove == "Y" or OpponentMove == "C" and OwnMove == "Z"):
        points += 3
    elif (OpponentMove == "A" and OwnMove == "Y" or OpponentMove == "B" and OwnMove == "Z" or OpponentMove == "C" and OwnMove == "X"):
        points += 6
    elif (OpponentMove == "A" and OwnMove == "Z" or OpponentMove == "B" and OwnMove == "X" or OpponentMove == "C" and OwnMove == "Y"):
        points += 0
print("First Half %d" % points)

"""
The Elf finishes helping with the tent and sneaks back over to you. 
"Anyway, the second column says how the round needs to end: X means you need to lose, 
Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

Following the Elf's instructions for the second column, 
what would your total score be if everything goes exactly according to your strategy guide?
"""

points2 = 0

for move in open("E:/Programacion/Python/AdventOfCode/AoC2/RockPaperScissors.txt", "r"):
    OpponentMove = move[0:1]
    #print(OpponentMove)
    OwnMove = move[1:-1]
    OwnMove = OwnMove.lstrip()
    #print(OwnMove)

    if (OpponentMove == "A" and OwnMove == "X"):
        points2 += 0 + 3
    elif(OpponentMove == "B" and OwnMove == "X"):
        points2 += 0 + 1
    elif(OpponentMove == "C" and OwnMove == "X"):
        points2 += 0 + 2

    if (OpponentMove == "A" and OwnMove == "Y"):
        points2 += 3 + 1
    elif(OpponentMove == "B" and OwnMove == "Y"):
        points2 += 3 + 2
    elif(OpponentMove == "C" and OwnMove == "Y"):
        points2 += 3 + 3

    if (OpponentMove == "A" and OwnMove == "Z"):
        points2 += 6 + 2
    elif(OpponentMove == "B" and OwnMove == "Z"):
        points2 += 6 + 3
    elif(OpponentMove == "C" and OwnMove == "Z"):
        points2 += 6 + 1
    
print("Seconds Half %d" % points2)
