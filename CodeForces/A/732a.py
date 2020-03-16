k,r = [int(i) for i in input().split()]
res = 1
while True:
    aux = k*res
    mod = aux % 10
    if mod != 0 and mod != r:
        res+=1
    else:
        break
print(str(res))
