from math import sqrt, ceil
num = int(input())
sqr = ceil(sqrt(num))+1
divs = []
for i in range(1, sqr):
    if num % i == 0:
        divs.append(i)
        divs.append(num//i)
divs.sort(reverse=1)
m = len(divs)
for i in range(m):
    tmp = divs[i]
    s = True
    for p in range(2, sqr):
        if tmp % p == 0:
            tmp /= p
        if tmp % p == 0:
            s = False
            break
    if s:
        print(divs[i])
        exit()
