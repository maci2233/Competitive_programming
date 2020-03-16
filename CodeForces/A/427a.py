n = int(input())
cases = [int(i) for i in input().split()]
police = 0
res = 0
for e in cases:
    if e != -1:
        police+=e
    else:
        if police == 0:
            res+=1
        else:
            police-=1
print(str(res))
