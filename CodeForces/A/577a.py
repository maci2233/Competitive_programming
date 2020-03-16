n,x = [int(i) for i in input().split()]
if n >= x:
    res = 1
else:
    res = 0
for i in range(2,n+1):
    if x % i == 0 and i*n >= x:
        res+=1
print(str(res))
