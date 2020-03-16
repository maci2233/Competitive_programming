n = int(input())
soldiers = [int(i) for i in input().split()]
max = soldiers[0]
min = soldiers[0]
indmin = 0
indmax = 0
res = 0
for i in range(1, n):
    if soldiers[i] > max:
        max = soldiers[i]
        indmax = i
    if soldiers[i] <= min:
        min = soldiers[i]
        indmin = i
res+=indmax + (n - 1 - indmin)
if indmax > indmin:
    res-=1
print(str(res))
