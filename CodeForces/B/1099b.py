import math
n = int(input())
if n <= 2:
    print(n+1)
    exit()
sqr = math.sqrt(n)
if sqr == int(sqr):
    print(int(sqr+sqr))
    exit()
else:
    sqr1 = math.ceil(math.sqrt(n))
    sqr2 = sqr1 - 1
    opt1 = sqr1 + math.ceil(n/sqr1)
    opt2 = sqr2 + math.ceil(n/sqr2)
    print(min(opt1, opt2))
