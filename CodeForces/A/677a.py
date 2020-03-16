test = input().split()
n = int(test[0])
h = int(test[1])
friends = [int(i) for i in input().split()]
res = 0
for e in friends:
    res+=1
    if e > h:
        res+=1
print(str(res))
