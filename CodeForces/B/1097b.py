sols = [0]
n = 1
t = int(input())
for _ in range(t):
    num = int(input())
    for i in range(n):
        sols.append(sols[i] + num)
        sols[i] -= num
    n *= 2
for e in sols:
    if e == 0 or e % 360 == 0:
        print('YES')
        exit()
print('NO')
