n = int(input())
l = 100002
nums = [int(i) for i in input().split()]
sums = [0 for i in range(l)]
res = [0 for i in range(l)]
for e in nums:
    sums[e]+=e
res[1] = sums[1]
res[2] = sums[2]
if res[2] < res[1]:
    res[2] = res[1]
for i in range(3,l):
    res[i] = sums[i]+res[i-2]
    if res[i] < res[i-1]:
        res[i] = res[i-1]
print(max(res))
