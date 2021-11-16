class Participant:
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.choice = ""
  def choose(self):
    self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
    print("{name} selects {choice}".format(name=self.name, choice = self.choice))
  def toNumericalChoice(self):
    switcher = {
    "rock": 0,
    "paper": 1,
    "scissor": 2
    }
    return switcher[self.choice]
  def incrementPoint(self):
    self.points += 1  

class GameRound:
  def __init__(self, p1, p2):
    self.rules = [
        [0, -1, 1],  #    0,0  0,1  0,2
        [1, 0, -1],  #    1,0  1,1  1,2
        [-1, 1, 0]   #    2,0  2,1  2,2 
    ]
    p1.choose()
    p2.choose()
    result = self.compareChoices(p1,p2)
    print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))
    if result > 0:
        p1.incrementPoint()
    elif result < 0:
        p2.incrementPoint()
  def compareChoices(self, p1, p2):
    v1= p1.toNumericalChoice()
    v2= p2.toNumericalChoice() 
    v3= self.rules[v1][v2]
    return v3
  def awardPoints(self):
      
    print("implement")
  def getResultAsString(self, result):
    res = {
        0: "draw",
        1: "win",
        -1: "loss"
    }
    return res[result]  

class Game:
  def __init__(self):
    self.endGame = False
    self.participant = Participant("Spock")
    self.secondParticipant = Participant("Kirk")
  def start(self):
    while not self.endGame:
        GameRound(self.participant, self.secondParticipant)
        self.checkEndCondition()
  def checkEndCondition(self):
    if input("Continue game y/n:")=="n":
        self.endGame = True
        print("Game ended, Spock has " + str(self.participant.points) + ", and Kirk has " + str(self.secondParticipant.points))
        self.determineWinner()
    # print("implement")
  def determineWinner(self):
    resultString = "It's a Draw"
    if self.participant.points > self.secondParticipant.points:
        resultString = "Winner is {name}".format(name=self.participant.name)
    elif self.participant.points < self.secondParticipant.points:
        resultString = "Winner is {name}".format(name=self.secondParticipant.name)
    print(resultString)

game = Game()
game.start()


