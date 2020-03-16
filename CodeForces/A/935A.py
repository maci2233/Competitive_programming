n = int(input())
res = 1
for i in range(2, n//2 + 1):
    m = n - i
    if m % i == 0:
        res += 1
print(res)
