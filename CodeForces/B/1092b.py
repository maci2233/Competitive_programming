n = int(input())
studs = [int(i) for i in input().split()]
studs.sort()
res = 0
for i in range(0,n,2):
    res += studs[i+1] - studs[i]
print(str(res))
