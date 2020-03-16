import bisect
input()
bottles = [int(i) for i in input().split()]
bottles.sort()
d = int(input())
res = ''
for _ in range(d):
    f = int(input())
    res+=str(bisect.bisect_right(bottles,f)) + '\n'
print(res)
