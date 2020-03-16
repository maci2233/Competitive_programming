n = int(input())
tot = n
hs = [0]*1005
for e in map(int, input().split()):
    hs[e] += 1
    if hs[e] > 1:
        tot -= 1
print(str(max(hs)) + ' ' + str(tot))
