n,k = [int(i) for i in input().split()]
studs = [int(i) for i in input().split()]
studs.sort()
res = 0
count = 0
for e in studs:
    if e+k <= 5:
        count+=1
        if count == 3:
            res+=1
            count=0
print(str(res))
