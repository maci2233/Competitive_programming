def flowers():
    n = int(input())
    if n == 0:
        return 0
    lens = [int(i) for i in input().split()]
    lens.sort(reverse=True)
    sum = 0
    tot = 0
    for e in lens:
        sum+=e
        tot+=1
        if sum >= n:
            return tot
    return -1

print(str(flowers()))
