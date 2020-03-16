n = int(input())
act = [int(i) for i in input().split()]
rest = 0
curr = 0
for e in act:
    if e == 0:
        rest += 1
        curr = 0
    elif e == 1:
        if curr == 0 or curr == 1:
            curr = -1
        else:
            rest += 1
            curr = 0
    elif e == 2:
        if curr == 0 or curr == -1:
            curr = 1
        else:
            rest += 1
            curr = 0
    else:
        if curr == 0:
            continue
        else:
            curr *= -1
print(rest)
