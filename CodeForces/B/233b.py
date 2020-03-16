n = int(input())
res = -1
for x in range(1,n):
    number = str(x)
    s = 0
    digits = [int(i) for i in number]
    s = sum(digits)
    if (x*x)+(s*x)-n == 0:
        res = x
        break
print(str(res))
