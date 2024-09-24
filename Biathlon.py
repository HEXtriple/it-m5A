from random import randint

shots = 5
targets = [1,2,3,4,5]

for i in range(shots):
    print("Select target:")
    target = int(input())- 1
    if(randint(1,2) == 1):
        targets[target] = 0
        print("Hit")
    else:
        print("Miss")

for target in targets:
    print("O" if target == 0 else "#")