import math

x = int(input())
solved = False
for b in range(1, x+1):
    for a in range(b, x+1):
        if a % b == 0 and a*b > x and a/b < x:
            solved = True
            break
    if solved:
        break
if solved:
    print(str(a) + ' ' + str(b))
else:
    print("-1")
