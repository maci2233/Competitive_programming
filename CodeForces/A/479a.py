a = int(input())
b = int(input())
c = int(input())
res = a+(b*c)
aux = a*(b+c)
if aux > res:
    res = aux
aux = a*b*c
if aux > res:
    res = aux
aux = a+b+c
if aux > res:
    res = aux
aux = (a+b)*c
if aux > res:
    res = aux
print(str(res))
