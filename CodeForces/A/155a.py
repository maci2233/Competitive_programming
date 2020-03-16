n = int(input())
scores = [int(i) for i in input().split()]
min = scores[0]
max = scores[0]
res = 0
for i in range(1,n):
    if scores[i] > max:
        res+=1
        max = scores[i]
    if scores[i] < min:
        res+=1
        min = scores[i]
print(str(res))
