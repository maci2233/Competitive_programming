n,k = [int(i) for i in input().split()]
walks = [int(i) for i in input().split()]
extra = 0
for i in range(1,n):
    tot = walks[i] + walks[i-1]
    if tot < k:
        dif = k - tot
        walks[i] += dif
        extra += dif
res = str(extra) + '\n'
for e in map(str, walks):
    res+=e + ' '
print(res)
