from math import sqrt
for _ in range(int(input())):
    a = -1
    b = int(input())
    if b == 0:
        print('Y 0 0')
        continue
    c = b*-1
    s = b**2 - 4*a*c
    if s < 0:
        print('N')
        continue
    n1 = (-b - sqrt(s)) / 2*a
    n2 = (-b + sqrt(s)) / 2*a
    print('Y ', n1, ' ', n2)
