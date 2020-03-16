import math

num = int(input())
res = math.ceil(num/2)
if num % 2 == 0:
    print(str(res))
else:
    print(str(res*-1))
