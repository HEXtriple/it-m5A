from random import randint

shots = 0
targets = [1,2,3,4,5]
odds = 70

def kollaTraff(odds):
    return randint(1,100) <= odds #slumpar med odds som sannolikhet i % (abstraktion)

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

def selectRounds(): #bestäm hur många rundor eller skott som spelaren ska ha (abstraktion)
    global shots
    shots = selectInput(1, 10, "rounds")

def startGame():
    for i in range(shots): #loop för alla rundor (repetition)
        target = selectInput(0, len(targets), "target")
        if(kollaTraff(odds)): #alternativ
            odds -= 10 #minska oddsen för att träffa
            if(targets[target] == 0):
                print("Hit on closed target")
            else:
                print("Hit")
            targets[target] = 0 #om träff, sätt värdet på elementet i arrayen till 0 
        else:
            print("Miss")

def printScore(): #skriv ut poäng
    score = ""
    for target in targets:
        score +=("O" if target == 0 else "#") + " "
    print(score)

#sekvens
selectRounds() 
startGame()
printScore()