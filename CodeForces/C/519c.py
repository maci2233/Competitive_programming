n,m = [int(i) for i in input().split()]
res = 0
while n > 0 and m > 0 and n+m >= 3:
    res+=1
    if n > m:
        n-=2
        m-=1
    else:
        n-=1
        m-=2
print(str(res))
