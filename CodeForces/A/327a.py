def coins():
    n = int(input())
    coin = [int(i) for i in input().split()]
    if n == 1:
        return 0 if coin[0] == 1 else 1
    su = sum(coin)
    if su == n:
        return n-1
    flip = [0 if i == 1 else 1 for i in coin]
    no_flip = [0]*n
    for i in range(1,n):
        no_flip[i] = coin[i-1] + no_flip[i-1]
    no_flip_r = [0]*n
    for i in range(n-2, 0, -1):
        no_flip_r[i] = coin[i+1] + no_flip_r[i+1]
    max = 0
    for i in range(n):
        aux = 0
        tot = 0
        for j in range(i,n):
            aux+=flip[j]
            test = aux + no_flip_r[j] + no_flip[i]
            if test > tot:
                tot = test
        if tot > max:
            max = tot
    return max

print(str(coins()))
