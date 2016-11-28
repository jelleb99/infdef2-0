class Game:
    def __init__(self,title, player1,player2):
        self.Player1 = player1
        self.Player2 = player2
        self.Title = title
class Player:
    def __init__(self,name,score):
        self.Name = name
        self.score = score
class RockPaperScissors:
    def __init__(self,player1,player2,winner):
        self.Player1 = player1
        self.Player2 = player2
        self.Winner = winner
paper = 0
rock = 1
scissors = 2
p1 = 0
p2 = 0

while p1 <= 2 and p2 <= 2:
    from random import randint
    x = (randint(0,2))
    y = (randint(0,2))
    if x == y:
        print("Draw")
    elif x == 1 and y == 2:
        p1 += 1
        print("player 1 wins this round")
    elif x == 1 and y == 0:
        p2 += 1
        print("player 2 wins this round")
    elif x == 0 and y == 1:
        p1 += 1
        print("player 1 wins this round")
    elif x ==0 and y ==2:
        p2 += 1
        print("player 2 wins this round")
    elif x == 2 and y == 1:
        p2 += 1
        print("player 2 wins this round")
    elif x ==2 and y == 0:
        p1 += 1
        print("player 1 wins this round")
    if p1 == 3:
        print("player 1 wins the game")
    if p2 == 3:
        print("player 2 wins the game")
