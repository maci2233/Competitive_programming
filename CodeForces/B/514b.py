from math import atan, degrees

n,x1,y1 = [int(i) for i in input().split()]
angles = set()
c = 0
for _ in range(n):
    x2,y2 = [int(i) for i in input().split()]
    if x1 == x2:
        if 0 not in angles:
            angles.add(0)
            c += 1
    elif y1 == y2:
        if 90 not in angles:
            angles.add(90)
            c += 1
    else:
        ad = x2-x1
        op = y2-y1
        ang = degrees(atan(op/ad))
        if ang not in angles:
            angles.add(ang)
            c += 1
print(c)
