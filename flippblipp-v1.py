n = 40

def flippblipp(n):
    if (n%3) == 0:
        return "flipp"
    elif (n%5) == 0:
        return "blipp"
    else:
        return n


for _ in range(1, n + 1):
    print(flippblipp(_))

