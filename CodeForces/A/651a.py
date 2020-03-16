a,b = [int(i) for i in input().split()]
mins = 0
while (a >= 2 or b >= 2) and a > 0 and b > 0:
    mins += 1
    if a < b:
        a += 1
        b -= 2
    else:
        b += 1
        a -= 2
print(str(mins))
