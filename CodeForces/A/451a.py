def winner():
    test = input().split()
    n = int(test[0])
    m = int(test[1])
    mult = n*m
    turn = 1
    while mult > 0:
        mult = mult - (n + m - 1)
        n-=1
        m-=1
        turn*=-1
    if turn == -1:
        return "Akshat"
    else:
        return "Malvika"

print(winner())
