q = int(input())
res = ''
for _ in range(q):
    mult = 1
    l,r,d = [int(i) for i in input().split()]
    if d < l:
        new = d
        res += str(new) + '\n'
    else:
        res += str(d * (r//d + 1)) + '\n'
print(res)
