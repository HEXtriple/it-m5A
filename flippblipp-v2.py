n = 10


def flippblipp(n):
    if (n%3 == 0 and n%5 == 0):
        return "flipp blipp"
    elif (n%3 == 0 and n%5 != 0):
        return "flipp"
    elif (n%3 != 0 and n%5 == 0):
        return "blipp"
    else:
        return str(n)


for _ in range(1, n + 1):
    print(flippblipp(_))

