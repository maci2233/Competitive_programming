n = int(input())
res = 1
aux = 1
h1 = input()
for _ in range(n-1):
    h2 = input()
    if h1 == h2:
        aux += 1
        if aux > res:
            res = aux
    else:
        aux = 1
    h1 = h2
print(str(res))
