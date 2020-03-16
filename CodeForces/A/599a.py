d1,d2,d3 = [int(i) for i in input().split()]
s1 = False
s2 = False
total = 0
if d1 < d2:
    total+=d1
    s1 = True
else:
    total+=d2
    s2 = True
if d1+d2 < d3:
    total+=d1+d2
else:
    total+=d3
if s1:
    if d3+d1 < d2:
        total+=d3+d1
    else:
        total+=d2
else:
    if d3+d2 < d1:
        total+=d3+d2
    else:
        total+=d1
print(str(total))
