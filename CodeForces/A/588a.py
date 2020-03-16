n = int(input())
meat = [0]*100002
cost = [0]*100002
for i in range(n):
    meat[i], cost[i] = [int(i) for i in input().split()]
i = 0
j = 0
res = 0
while i < n:
    if i == j:
        res+=meat[i] * cost[j]
        i+=1
    while cost[j] < cost[i] and i < n:
        res+=meat[i] * cost[j]
        i+=1
    j=i
print(str(res))
