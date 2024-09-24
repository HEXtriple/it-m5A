from random import randint

shots = 5
targets = [1,2,3,4,5]
odds = 70

def kollaTraff(odds):
    return randint(1,100) <= odds

for i in range(shots):
    print("Select target:")
    target = -1
    selectedTarget = -1
    while(target == -1):
        try:
            selectedTarget = int(input())- 1
        except:
            print("Invalid target")
            continue
        if(selectedTarget < 0 or selectedTarget > len(targets)):
            print("Invalid target")
            continue
        target = selectedTarget
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