from random import randint

class Player:
    shots = 0
    targets = [1,2,3,4,5]
    odds = 70
    def kollaTraff(odds):
        return randint(1,100) <= odds

players = []
numberOfPlayers = 0


def selectInput(min,max, type):
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

def selectRounds():
    global shots
    shots = selectInput(1, 10, "rounds")



def startGame():
    selectRounds()
    global numberOfPlayers
    numberOfPlayers = selectInput(1, 10, "number of players") + 1
    for _ in range(numberOfPlayers):
        player = Player
        players.append(player)
    for _ in range(shots):
        for _ in range(len(players)):
            p = players[_]
            print("Player " + str(_ + 1))
            target = selectInput(0, len(p.targets), "target")
            if(p.kollaTraff(p.odds)):
                p.odds -= 10
                if(p.targets[target] == 0):
                    print("Hit on closed target")
                else:
                    print("Hit")
                p.targets[target] = 0
            else:
                print("Miss")
    for _ in range(len(players)):
        p = players[_]
        score = ""
        for target in p.targets:
            score +=("O" if target == 0 else "#") + " "
        print(score)

startGame()


