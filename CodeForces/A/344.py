n = int(input())
magnets = []
res = 1
for i in range(n):
    magnets.append(input())
for i in range(n-1):
    if magnets[i][1] == magnets[i+1][0]:
        res+=1
print(str(res))
