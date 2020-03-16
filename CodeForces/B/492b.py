n,l = [int(i) for i in input().split()]
lanterns = sorted([int(i) for i in input().split()])
res = (lanterns[0] - 0)
for i in range(1, n):
    aux = (lanterns[i] - lanterns[i-1]) / 2
    if aux > res:
        res = aux
aux = l - lanterns[n-1]
if aux > res:
    res = aux
print(str(res))
