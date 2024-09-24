def flipporblipp(n):
    if (n%3) == 0:
        return "flipp"
    elif (n%5) == 0:
        return "blipp"
    else:
        return n


for i in range(1, 40):
    print(flipporblipp(i))

