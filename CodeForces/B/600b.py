from bisect import bisect_right

input()
a = sorted([int(i) for i in input().split()])
b = [int(i) for i in input().split()]
res = ''
for num in b:
    res += str(bisect_right(a, num)) + ' '
print(res)
