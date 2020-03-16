from math import ceil
n = int(input())
t = ceil(n/2)
print('0' if t % 2 == 0 else '1')
