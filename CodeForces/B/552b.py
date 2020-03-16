num = int(input())
n = len(str(num))
lim = [0,0,9,99,999,9999,99999,999999,9999999,99999999,999999999,9999999999]
acum = 0
while num > 0:
    dif = num - lim[n]
    acum += (dif * n)
    num = lim[n]
    n -= 1
print(acum)
