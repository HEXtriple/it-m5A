def flippblipp(n):
    if (n%3 == 0 and n%5 == 0):
        return "flipp blipp"
    elif (n%3 == 0 and n%5 != 0):
        return "flipp"
    elif (n%3 != 0 and n%5 == 0):
        return "blipp"
    else:
        return str(n)


#Game
def rungame():
    n = 1
    print(n)
    while True:
        n +=1
        guess = str(input('Nästa: ')).lower()
        correctAnswer = flippblipp(n)
        
        if correctAnswer == guess:
            continue
        else:
            print("Fel -", correctAnswer)
            print(); print("Game over")
            break
            
rungame()
exit()