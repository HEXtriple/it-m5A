def flippblipp(n): #sekvens 2, abstraktion (bryt ner problemet)
    if (n%3 == 0 and n%5 == 0): #alternativ
        return "flipp blipp"
    elif (n%3 == 0 and n%5 != 0): #alternativ
        return "flipp"
    elif (n%3 != 0 and n%5 == 0): #alternativ
        return "blipp"
    else:
        return str(n)


#Game
def rungame(): #sekvens 1
    n = 1
    print(n)
    while True: #repetition 
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