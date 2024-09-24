from random import randint

shots = 0
targets = [1,2,3,4,5]
odds = 70

def kollaTraff(odds):
    return randint(1,100) <= odds

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

selectRounds()

for i in range(shots):
    target = selectInput(0, len(targets), "target")
    if(kollaTraff(odds)):
        odds -= 10
        if(targets[target] == 0):
            print("Hit on closed target")
        else:
            print("Hit")
        targets[target] = 0
    else:
        print("Miss")

score = ""
for target in targets:
    score +=("O" if target == 0 else "#") + " "
print(score)