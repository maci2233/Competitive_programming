c = [int(i) for i in input().split()]
res = 0
for e in map(int, input()):
    res+=c[e-1]
print(str(res))
