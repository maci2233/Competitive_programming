def kk():
    n = int(input())
    if n == 3:
        return '1 2 3'
    kids = [[] for i in range(n+1)]
    for i in range(1,n+1):
        a,b = [int(i) for i in input().split()]
        kids[i].append(a)
        kids[i].append(b)
    res = '1'
    curr = 1
    init = 1
    while n > 0:
        k1 = kids[curr][0]
        k2 = kids[curr][1]
        next = k1 if kids[k1][0] == k2 or kids[k1][1] == k2 else k2
        if next != init:
            res += ' ' + str(next)
            curr = next
        n -= 1
    return res

print(kk())
