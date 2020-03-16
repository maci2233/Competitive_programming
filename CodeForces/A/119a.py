def gcd(a, b):
    maxn = max(a,b)
    minn = min(a,b)
    if minn == 0:
        return maxn
    if maxn % minn == 0:
        return minn
    else:
        return gcd(minn,maxn % minn)

def main():
    a,b,n = [int(i) for i in input().split()]
    turn = 0
    gc = gcd(a,n)
    while n-gc >= 0:
        n-=gc
        if turn == 0:
            gc = gcd(b,n)
            turn = 1
        else:
            gc = gcd(a,n)
            turn = 0
    if turn == 0:
        turn = 1
    else:
        turn = 0
    print(str(turn))

main()
