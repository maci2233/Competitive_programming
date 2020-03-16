import math

test = input().split()
n = int(test[0])
k = int(test[1])
mid = math.ceil(n/2)
if k > mid:
    print(str((k-mid)*2))
else:
    print(str(k*2 - 1))
