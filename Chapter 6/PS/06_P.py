n = 5

for row in range(1, 2*n+1):
    TotalColInRow = 2*n-row if row > n else row
    NoOfSpaces = n - TotalColInRow
    for spaces in range(NoOfSpaces):
        print(" ", end='')
    for col in range(0, TotalColInRow):
        print("*", end=' ')
    print()