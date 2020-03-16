n,m,a,b = [int(i) for i in input().split()]
total = 0
if b/m <= a:
    limit = m
    cost = b
else:
    limit = 1
    cost = a
while n >= limit:
    n-=limit
    total+=cost
if n*a <= b:
    total+=n*a
else:
    total+=b
print(str(total))
