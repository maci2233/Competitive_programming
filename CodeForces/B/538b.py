n = int(input())
res = []
while n > 0:
    sn = str(n)
    tmp = ''
    for e in map(int, sn):
        tmp += '1' if e >= 1 else '0'
    n -= int(tmp)
    res.append(tmp)
print(len(res))
print(*res)
