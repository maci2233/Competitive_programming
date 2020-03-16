n = int(input())
bills = [100, 20, 10, 5, 1]
res = 0
i = 0
while n != 0:
    if n < bills[i]:
        i += 1
    else:
        div, mod = divmod(n, bills[i])
        res += div
        n = mod
print(res)
