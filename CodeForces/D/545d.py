n = int(input())
queue = [int(i) for i in input().split()]
queue.sort()
acum = queue[0]
res = n
for i in range(1, n):
    if acum > queue[i]:
        res -= 1
    else:
        acum += queue[i]
print(res)
