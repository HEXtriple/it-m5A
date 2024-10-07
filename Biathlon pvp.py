from random import randint

class Player: #Spelarklass, möjliggör för flera spelare att kunna spela.
    def __init__(self):
        self.shots = 0
        self.targets = [1, 2, 3, 4, 5]
        self.odds = 70
    def kollaTraff(self, odds):
        return randint(1,100) <= odds

players = []
numberOfPlayers = 0


def selectInput(min,max, type): #funktion för att välja ett värde inom ett intervall utan att programmet kraschar (abstraktion)
    selectedTarget = -1
    while(selectedTarget == -1):
        print("Select " + str(type) + ":")
        try:
            selectedTarget = int(input())- 1
        except:
            print("Invalid input")
            continue
        if(selectedTarget < min or selectedTarget > max):
            selectedTarget = -1
            print("Invalid input")
            continue
    return selectedTarget

def selectRounds(): #abstraktion
    global shots
    shots = selectInput(1, 10, "rounds")

def startGame(): #huvudloop
    global numberOfPlayers
    numberOfPlayers = selectInput(1, 10, "number of players") + 1
    for _ in range(numberOfPlayers): #lägg till rätt antal spelare i arrayen
        player = Player()
        players.append(player)
    for _ in range(shots): #loopa varje runda (repetition)
        for _ in range(len(players)): #loopa varje spelares tur (repetition)
            p = players[_]
            print("Player " + str(_ + 1))
            target = selectInput(0, len(p.targets), "target")
            if(p.kollaTraff(p.odds)): #alterativ
                p.odds -= 10 #minska sannolikheten för träff
                if(p.targets[target] == 0):
                    print("Hit on closed target")
                else:
                    print("Hit")
                p.targets[target] = 0 #om träff, sätt värdet på elemetet i arrayen till 0
            else:
                print("Miss")

def printScore():
    for _ in range(len(players)): #loopa och printa alla spelares poäng
        p = players[_]
        score = ""
        for target in p.targets:
            score +=("O" if target == 0 else "#") + " "
        print("Player" + str(_+1) + " " + score)

#Sekvens
selectRounds()
startGame()
printScore()


