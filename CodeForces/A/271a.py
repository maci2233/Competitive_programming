test = int(input())
res = 0
for y in range(test+1, 10000):
    year = str(y)
    n = len(year)
    for i in range(n-1):
        sum = 0
        for j in range(i+1, n):
            if year[i] == year[j]:
                sum+=1
        if sum > 0:
            break
    if sum == 0:
        res = year
        break

print(res)
