n = 20


def flippblipp(n): #abstraktion,
    if (n%3 == 0 and n%5 == 0): #alternativ
        return "flipp blipp"
    elif (n%3 == 0 and n%5 != 0): #alternativ
        return "flipp"
    elif (n%3 != 0 and n%5 == 0): #alternativ
        return "blipp"
    else:
        return str(n)


for _ in range(1, n + 1): #repetition
    print(flippblipp(_))

