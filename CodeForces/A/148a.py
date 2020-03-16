dmg = []
n = 4
for i in range(n):
    dmg.append(int(input()))
d = int(input())
res = set()
for e in dmg:
    num = e
    while(num <= d):
        if num not in res:
            res.add(num)
        num+=e
print(len(res))
