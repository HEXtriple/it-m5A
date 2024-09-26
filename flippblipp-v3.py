rounds = 40


def flippblipp(n):
    if (n%3) == 0 and (n%5) == 0:
        return "flipp blipp"
    elif (n%3 == 0 and n%5 != 0):
        return "flipp"
    elif (n%3 != 0 and n%5 == 0):
        return "blipp"
    else:
        return str(n)


#Game
def rungame(n):
    print("1")
    for _ in range(2, n + 1):
        
        guess = str(input('Nästa: ')).lower()
        correctAnswer = flippblipp(_)
        
        if correctAnswer == guess:
            continue
        else:
            print("Fel -", correctAnswer)
            print("Game over")
            exit()


rungame(rounds)